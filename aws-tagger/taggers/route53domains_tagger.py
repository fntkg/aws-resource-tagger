import boto3
from .base import AwsResourceTagger
from .registry import TaggerRegistry
from utils.arn_parser import AWSArnParser

# Concrete class for tagging Route53 domains
@TaggerRegistry.register("route53domains")
class Route53DomainTagger(AwsResourceTagger):
    def __init__(self, region: str):
        self.route53domains = boto3.client('route53domains', region_name=region)

    def tag_resource(self, arn: str, tags: list):
        try:
            self.route53domains.update_tags_for_domain(DomainName=AWSArnParser.get_resource_id(arn), TagsToUpdate=tags)
        except Exception as e:
            print(f"Error tagging {arn}: {e}")