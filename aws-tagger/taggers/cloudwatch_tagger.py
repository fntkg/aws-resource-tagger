import boto3
from .base import AwsResourceTagger
from .registry import TaggerRegistry
from arn_parser.arn_parser import AWSArnParser

# Concrete class for tagging Cloudwatch resources
@TaggerRegistry.register("cloudwatch")
class CloudwatchTagger(AwsResourceTagger):
    @staticmethod
    def tag_resource(arn: str, tags: list):
        print(f"Tagging Cloudwatch: {arn}")
        region = AWSArnParser.get_region(arn)
        alarm = boto3.client('cloudwatch', region_name=region)
        try:
            alarm.tag_resource(ResourceARN=arn, Tags=tags)
        except Exception as e:
            print(f"Error tagging Cloudwatch {arn}: {e}")