import boto3
from .base import AwsResourceTagger
from .registry import TaggerRegistry
from utils.arn_parser import AWSArnParser

# Concrete class for tagging Event Bridge resources
@TaggerRegistry.register("events")
class EventBridgeTagger(AwsResourceTagger):
    @staticmethod
    def tag_resource(arn: str, tags: list):
        region = AWSArnParser.get_region(arn)
        function = boto3.client('events', region_name=region)
        try:
            function.tag_resource(ResourceARN=arn, Tags=tags)
        except Exception as e:
            print(f"Error tagging {arn}: {e}")