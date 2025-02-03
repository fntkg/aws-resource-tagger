import boto3
from .base import AwsResourceTagger
from .registry import TaggerRegistry

# Concrete class for tagging Event Bridge resources
@TaggerRegistry.register("events")
class EventBridgeTagger(AwsResourceTagger):
    def __init__(self, region: str):
        self.events = boto3.client('events', region_name=region)

    def tag_resource(self, arn: str, tags: list):
        try:
            self.events.tag_resource(ResourceARN=arn, Tags=tags)
        except Exception as e:
            print(f"Error tagging {arn}: {e}")