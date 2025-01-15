from abc import ABC, abstractmethod

# Abstract base class for AWS resource tagging
class AwsResourceTagger(ABC):
    def __init__(self, resource_id, tags, region, account_id=None):
        self.resource_id = resource_id
        self.tags = tags
        self.region = region
        self.account_id = account_id

    @abstractmethod
    def add_tags(self):
        """Abstract method to add tags to a resource"""
        pass
