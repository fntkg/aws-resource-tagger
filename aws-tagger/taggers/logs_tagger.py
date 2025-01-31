import boto3
from .base import AwsResourceTagger
from utils.tag_formatter import adapt_tags
from .registry import TaggerRegistry
from arn_parser.arn_parser import AWSArnParser

# Concrete class for tagging CloudWatch resources
@TaggerRegistry.register("logs")
class LogsTagger(AwsResourceTagger):
    @staticmethod
    def tag_resource(arn: str, tags: list):
        formated_tags = adapt_tags(tags)
        region = AWSArnParser.get_region(arn)
        logs = boto3.client('logs', region_name=region)
        try:
            logs.tag_resource(resourceArn=f'{arn}', tags=formated_tags)
        except Exception as e:
            print(f"Error tagging {arn}: {e}")