import re


class AWSArnParser:
    """
    Utility class for parsing and extracting components from AWS ARNs (Amazon Resource Names).

    This class provides static methods to validate and extract different parts of an ARN,
    such as the service, region, account ID, resource type, and resource ID. It ensures
    ARNs follow the expected format and enables easy retrieval of specific components.
    """

    ARN_REGEX = re.compile(
        r"^arn:(?P<partition>[^:]+):(?P<service>[^:]+):(?P<region>[^:]*):(?P<account_id>[^:]*):(?P<resource>.+)$"
    )
    """Regular expression pattern to match and extract components from an AWS ARN."""

    @staticmethod
    def parse_arn(arn: str) -> dict:
        """
        Parses an AWS ARN and extracts its components.

        Args:
            arn (str): The ARN string to be parsed.

        Returns:
            dict: A dictionary containing the extracted ARN components, including:
                - partition (str)
                - service (str)
                - region (str) (may be empty for global services)
                - account_id (str) (may be empty for global resources)
                - resource (str)

        Raises:
            ValueError: If the ARN does not match the expected format.
        """
        match = AWSArnParser.ARN_REGEX.match(arn)
        if not match:
            raise ValueError(f"Invalid ARN: {arn}")
        return match.groupdict()

    @staticmethod
    def get_service(arn: str) -> str:
        """
        Extracts the AWS service name from the ARN.

        Args:
            arn (str): The ARN string to be parsed.

        Returns:
            str: The AWS service name (e.g., 's3', 'ec2', 'lambda').
        """
        return AWSArnParser.parse_arn(arn).get("service") or None

    @staticmethod
    def get_region(arn: str) -> str:
        """
        Extracts the AWS region from the ARN.

        Args:
            arn (str): The ARN string to be parsed.

        Returns:
            str: The AWS region (e.g., 'us-east-1', 'eu-west-1') or None if not applicable.
        """
        return AWSArnParser.parse_arn(arn).get("region") or None

    @staticmethod
    def get_account_id(arn: str) -> str:
        """
        Extracts the AWS account ID from the ARN.

        Args:
            arn (str): The ARN string to be parsed.

        Returns:
            str: The AWS account ID or None if not applicable.
        """
        return AWSArnParser.parse_arn(arn).get("account_id") or None

    @staticmethod
    def get_resource_type(arn: str) -> str:
        """
        Extracts the resource type from the ARN.

        The resource part of an ARN can be formatted as `resourceType/resourceId`
        or `resourceType:resourceId`. This method extracts the `resourceType` part.

        Args:
            arn (str): The ARN string to be parsed.

        Returns:
            str: The resource type (e.g., 'instance', 'function', 'bucket').
        """
        resource = AWSArnParser.parse_arn(arn).get("resource")
        if "/" in resource:
            return resource.split("/")[0]
        elif ":" in resource:
            return resource.split(":")[0]
        return resource

    @staticmethod
    def get_resource_id(arn: str) -> str:
        """
        Extracts the resource ID from the ARN.

        The resource part of an ARN can be formatted as:
        - `resourceType/resourceId`
        - `resourceType:resourceId`
        - Just `resourceId` in some cases

        This method extracts the `resourceId` from the ARN.

        Args:
            arn (str): The ARN string to be parsed.

        Returns:
            str: The resource ID (e.g., an EC2 instance ID, Lambda function name, or S3 bucket name).
        """
        resource = AWSArnParser.parse_arn(arn).get("resource")
        if "/" in resource:
            return resource.split("/")[1]
        elif ":" in resource:
            return resource.split(":")[1]
        return resource

    @staticmethod
    def fix_arn(arn: str) -> str:
        """
        Parses and corrects the ARN when it represents an AWS email-related resource.

        Some tools generate ARNs incorrectly, particularly for AWS Workspaces SES resources.
        This method corrects such cases by making the following modifications:

        - If the service is identified as 'workspaces' and the resource type as 'ses',
          it replaces 'ses' with 'identity' and swaps 'workspaces' with 'ses'.

        Args:
            arn (str): The original ARN string.

        Returns:
            str: The corrected ARN string.
        """
        if AWSArnParser.get_service(arn) == 'workspaces' and AWSArnParser.get_resource_type(arn) == 'ses':
            arn = arn.replace('ses', 'identity')
            arn = arn.replace('workspaces', 'ses')
        return arn
