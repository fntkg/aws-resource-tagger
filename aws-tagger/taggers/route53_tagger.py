import boto3
from .base import AwsResourceTagger
from .registry import TaggerRegistry
from utils.arn_parser import AWSArnParser

# Concrete class for tagging Route53 resources (except domains)
@TaggerRegistry.register("route53")
class Route53Tagger(AwsResourceTagger):
    def __init__(self, region: str):
        self.route53 = boto3.client('route53', region_name=region)

    def tag_resource(self, arn: str, tags: list):
        try:
            self.route53.change_tags_for_resource(
                ResourceType=AWSArnParser.get_resource_type(arn),
                ResourceId=AWSArnParser.get_resource_id(arn),
                AddTags=tags
            )
        except Exception as e:
            print(f"Error tagging {arn}: {e}")