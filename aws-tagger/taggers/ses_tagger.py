import boto3
from .base import AwsResourceTagger
from .registry import TaggerRegistry
from arn_parser.arn_parser import AWSArnParser

# Concrete class for tagging SES Resources
@TaggerRegistry.register("ses")
class WorkspacesTagger(AwsResourceTagger):
    @staticmethod
    def tag_resource(arn: str, tags: list):
        ses = boto3.client('sesv2', region_name=AWSArnParser.get_region(arn))
        try:
            ses.tag_resource(ResourceArn=arn, Tags=tags)
        except Exception as e:
            print(f"Error tagging {arn}: {e}")