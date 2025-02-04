import csv

from utils.arn_parser import AWSArnParser
from .base import BaseParser
from .registry import ParserRegistry

@ParserRegistry.register("wiz")
class CSVWizParser(BaseParser):
    """
    A parser class for processing CSV files generated by Wiz that contain AWS resources.

    This class extends the `BaseParser` class and is registered in the `ParserRegistry` under the name "wiz".
    It reads a CSV file, identifies AWS resource ARNs using a column ending with "providerUniqueId",
    and returns a list of these resource ARNs.

    Methods:
        parse(file_path: str) -> list:
            Parses a Wiz-generated CSV file and extracts AWS resource ARNs.

    Example:
        parser = ParserRegistry.get_parser("wiz")
        resources = parser.parse("wiz_aws_resources.csv")
    """

    @staticmethod
    def parse(file_path: str) -> list:
        """
        Parses a Wiz-generated CSV file to extract AWS resource ARNs.

        Args:
            file_path (str): The file path to the Wiz-generated CSV file.

        Returns:
            list: A list of AWS resource ARNs extracted from the file.

        Raises:
            KeyError: If no column ending with "providerUniqueId" is found in the CSV file.
        """
        resources = []
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Identify required columns using suffix search
                resource_arn_column = next((col for col in row if col.endswith("providerUniqueId")), None)
                if not resource_arn_column:
                    raise KeyError("No column ending with 'providerUniqueId' found in the CSV file.")
                region_column = next((col for col in row if col.endswith("region")), None)
                if not region_column:
                    raise KeyError("No column ending with 'region' found in the CSV file.")
                resource_arn = row[resource_arn_column]
                region = row[region_column]
                resource_arn = CSVWizParser.__fix_arn(resource_arn, region)
                resources.append(resource_arn)
        return resources

    @staticmethod
    def __fix_arn(arn: str, region: str) -> str:
        """
        Parses and corrects the ARN.

        Args:
            arn (str): The original ARN string.

        Returns:
            str: The corrected ARN string.
        """
        if arn.startswith('key-'):
            # This is an SSH Key pair
            arn = f'arn:aws:ec2:{region}:0000:key-pair/{arn}'

        if arn.startswith('rtb-'):
            # This is a Route Table
            arn = f'arn:aws:ec2:{region}:0000:route-table/{arn}'

        if AWSArnParser.get_service(arn) == 'workspaces' and AWSArnParser.get_resource_type(arn) == 'ses':
            arn = arn.replace('ses', 'identity')
            arn = arn.replace('workspaces', 'ses')
        return arn