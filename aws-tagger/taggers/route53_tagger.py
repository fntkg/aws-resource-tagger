import boto3
from .base import AwsResourceTagger
from .registry import TaggerRegistry
from utils.arn_parser import AWSArnParser

# Concrete class for tagging Route53 resources (except domains)
@TaggerRegistry.register("route53")
class Route53Tagger(AwsResourceTagger):
    @staticmethod
    def tag_resource(arn: str, tags: list):
        region = AWSArnParser.get_region(arn)
        resource_type = AWSArnParser.get_resource_type(arn)
        resource_id = AWSArnParser.get_resource_id(arn)
        route53 = boto3.client('route53', region_name=region)
        try:
            route53.change_tags_for_resource(ResourceType=resource_type, ResourceId=resource_id, AddTags=tags)
        except Exception as e:
            print(f"Error tagging {arn}: {e}")