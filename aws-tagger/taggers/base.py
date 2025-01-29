from abc import ABC, abstractmethod


class AwsResourceTagger(ABC):
    """
    Abstract base class to handle tagging of AWS resources.
    """

    @staticmethod
    @abstractmethod
    def tag_resource(arn: str, tags: list):
        """
        Abstract method to add tags_file to a resource.

        Args:
            arn (str): The unique identifier of the AWS resource.
            tags (list): A list of key-value pairs representing the tags_file to be applied.
        """
        pass
