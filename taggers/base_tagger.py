from abc import ABC, abstractmethod

# Abstract base class for AWS resource tagging
class AwsResourceTagger(ABC):
    def __init__(self, resource_id, tags, region):
        self.resource_id = resource_id
        self.tags = tags
        self.region = region

    @abstractmethod
    def add_tags(self):
        """Abstract method to add tags to a resource"""
        pass
