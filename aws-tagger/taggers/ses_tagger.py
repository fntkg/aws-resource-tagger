import boto3
from .base import AwsResourceTagger
from .registry import TaggerRegistry
from utils.arn_parser import AWSArnParser

# Concrete class for tagging SES Resources
@TaggerRegistry.register("ses")
class WorkspacesTagger(AwsResourceTagger):
    def __init__(self, region: str):
        self.sesv2 = boto3.client('sesv2', region_name=region)

    def tag_resource(self, arn: str, tags: list):
        try:
            self.sesv2.tag_resource(ResourceArn=arn, Tags=tags)
        except Exception as e:
            print(f"Error tagging {arn}: {e}")