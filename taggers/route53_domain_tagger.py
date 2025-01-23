import boto3
from .base_tagger import AwsResourceTagger
from utils.id_formatter import extract_resource_name

# Concrete class for tagging Route53 domains
class Route53DomainTagger(AwsResourceTagger):
    def add_tags(self):
        print(f"Tagging Route53 domain: {self.resource_arn} in region {self.region}")
        resource_id = extract_resource_name(self.resource_arn)
        route53domains = boto3.client('route53domains', region_name=self.region)
        try:
            route53domains.update_tags_for_domain(DomainName=resource_id, TagsToUpdate=self.tags)
        except Exception as e:
            print(f"Error tagging Route53 domain {self.resource_arn}: {e}")