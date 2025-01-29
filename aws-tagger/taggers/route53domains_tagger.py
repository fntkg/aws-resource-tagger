import boto3
from .base import AwsResourceTagger
from .registry import TaggerRegistry
from arn_parser.arn_parser import AWSArnParser

# Concrete class for tagging Route53 domains
@TaggerRegistry.register("route53domains")
class Route53DomainTagger(AwsResourceTagger):
    @staticmethod
    def tag_resource(arn: str, tags: list):
        print(f"Tagging Route53 domain: {arn}")
        region = AWSArnParser.get_region(arn)
        resource_id = AWSArnParser.get_resource_id(arn)
        route53domains = boto3.client('route53domains', region_name=region)
        try:
            route53domains.update_tags_for_domain(DomainName=resource_id, TagsToUpdate=tags)
        except Exception as e:
            print(f"Error tagging Route53 domain {arn}: {e}")