import boto3
from .base import AwsResourceTagger
from utils.tag_formatter import adapt_tags
from .registry import TaggerRegistry

# Concrete class for tagging CloudWatch resources
@TaggerRegistry.register("logs")
class LogsTagger(AwsResourceTagger):
    def __init__(self, region: str):
        self.logs = boto3.client('logs', region_name=region)

    def tag_resource(self, arn: str, tags: list):
        try:
            self.logs.tag_resource(resourceArn=f'{arn}', tags=adapt_tags(tags))
        except Exception as e:
            print(f"Error tagging {arn}: {e}")