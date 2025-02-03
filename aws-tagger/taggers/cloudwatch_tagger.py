import boto3
from .base import AwsResourceTagger
from .registry import TaggerRegistry

# Concrete class for tagging Cloudwatch resources
@TaggerRegistry.register("cloudwatch")
class CloudwatchTagger(AwsResourceTagger):
    def __init__(self, region: str):
        self.cloudwatch = boto3.client('cloudwatch', region_name=region)

    def tag_resource(self, arn: str, tags: list):
        try:
            self.cloudwatch.tag_resource(ResourceARN=arn, Tags=tags)
        except Exception as e:
            print(f"Error tagging {arn}: {e}")