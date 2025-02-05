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
    and returns a list of these resource ARNs after applying necessary corrections.

    Methods:
        parse(file_path: str) -> list:
            Parses a Wiz-generated CSV file and extracts AWS resource ARNs.
    """

    @staticmethod
    def parse(file_path: str) -> list:
        """
        Parses a Wiz-generated CSV file to extract AWS resource ARNs.

        This method reads a CSV file where each row represents an AWS resource with various properties.
        It extracts required fields such as the resource ARN, region, resource type, name, and account ID,
        and then fixes the ARN if needed based on the resource type.

        Args:
            file_path (str): The file path to the Wiz-generated CSV file.

        Returns:
            list: A list of AWS resource ARNs extracted from the file.

        Raises:
            KeyError: If a necessary column (determined by a suffix such as "providerUniqueId") is not found.
        """
        resources = []
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                resource_arn = CSVWizParser.__get_column_value(row, "providerUniqueId")
                region = CSVWizParser.__get_column_value(row, "region")
                resource_type = CSVWizParser.__get_column_value(row, "nativeType")
                name = CSVWizParser.__get_column_value(row, "Name")
                account_id = CSVWizParser.__get_column_value(row, "subscriptionExternalId")

                # Fix the ARN if necessary based on the resource type and other attributes.
                resource_arn = CSVWizParser.__fix_arn(resource_arn, region, resource_type, name, account_id)
                resources.append(resource_arn)
        return resources

    @staticmethod
    def __fix_arn(arn: str, region: str, resource_type: str, name: str, account_id: str) -> str:
        """
        Parses and corrects the ARN based on the resource type and other attributes.

        Depending on the resource type or specific patterns in the ARN, this method constructs
        the correct ARN string for the resource. For example, it handles ECR repositories,
        EC2 key pairs, EC2 route tables, and adjustments for SES Email Identities.

        Args:
            arn (str): The original ARN string.
            region (str): The AWS region of the resource.
            resource_type (str): The type of the AWS resource.
            name (str): The name of the resource.
            account_id (str): The AWS account ID associated with the resource.

        Returns:
            str: The corrected ARN string.
        """
        if resource_type == 'repository':
            # This is an ECR Repository
            return f'arn:aws:ecr:{region}:{account_id}:repository/{name}'

        if arn.startswith('key-'):
            # This is an EC2 Key Pair
            return f'arn:aws:ec2:{region}:{account_id}:key-pair/{arn}'

        if arn.startswith('rtb-'):
            # This is a Route Table
            return f'arn:aws:ec2:{region}:{account_id}:route-table/{arn}'

        if AWSArnParser.get_service(arn) == 'workspaces' and AWSArnParser.get_resource_type(arn) == 'ses':
            # This is a SES Email Identity; adjust the ARN accordingly.
            arn = arn.replace('ses', 'identity')
            arn = arn.replace('workspaces', 'ses')
            return arn

        return arn

    @staticmethod
    def __get_column_value(row: dict, suffix: str) -> str:
        """
        Retrieves the value from a CSV row for the column whose header ends with the specified suffix.

        This helper method iterates through the keys in the given CSV row (a dictionary)
        and returns the value of the first column name that ends with the provided suffix.
        If no matching column is found, it raises a KeyError.

        Args:
            row (dict): A dictionary representing a row from the CSV file, where keys are column headers.
            suffix (str): The suffix to match in the column header.

        Returns:
            str: The value corresponding to the column with a header ending in the specified suffix.

        Raises:
            KeyError: If no column with a header ending in the specified suffix is found.
        """
        column_name = next((col for col in row if col.endswith(suffix)), None)
        if not column_name:
            raise KeyError(f"Column ending with '{suffix}' not found in row: {row}")
        return row[column_name]
