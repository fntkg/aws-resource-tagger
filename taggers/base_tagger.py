from abc import ABC, abstractmethod


# Abstract base class for AWS resource tagging
class AwsResourceTagger(ABC):
    """
    Abstract base class to handle tagging of AWS resources.

    Attributes:
        resource_id (str): The unique identifier of the AWS resource.
        tags (list): A list of key-value pairs representing the tags to be applied.
        region (str, optional): The AWS region where the resource is located. Defaults to None.
        account_id (str, optional): The AWS account ID that owns the resource. Defaults to None.
    """

    def __init__(self, resource_id, tags, region=None, account_id=None, full_resource_id=None):
        """
        Initializes the AwsResourceTagger instance with resource details and tags.

        Args:
            resource_id (str): The unique identifier of the AWS resource.
            tags (list): A list of key-value pairs representing the tags to be applied.
            region (str, optional): The AWS region of the resource. Defaults to None.
            account_id (str, optional): The AWS account ID. Defaults to None.
        """
        self.resource_id = resource_id
        self.tags = tags
        self.region = region
        self.account_id = account_id
        self.full_resource_id = full_resource_id

    @abstractmethod
    def add_tags(self):
        """
        Abstract method to add tags to a resource.

        This method must be implemented by subclasses to provide the logic for
        tagging AWS resources.
        """
        pass
