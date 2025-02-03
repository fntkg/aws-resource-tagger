from abc import ABC, abstractmethod

class AwsResourceTagger(ABC):
    """
    Abstract base class to handle tagging of AWS resources.

    Subclasses must implement a constructor that accepts a `region` parameter,
    even if it is not used internally.
    """

    @abstractmethod
    def __init__(self, region: str):
        """
        Constructor that must be implemented by all subclasses.

        Args:
            region (str): The AWS region where the resource is located.
        """
        pass

    @abstractmethod
    def tag_resource(self, arn: str, tags: list) -> None:
        """
        Abstract method to add tags to a resource.

        Args:
            arn (str): The unique identifier of the AWS resource.
            tags (list): A list of key-value pairs representing the tags to be applied.
        """
        pass
