import boto3
from .base_tagger import AwsResourceTagger

# Concrete class for tagging Route53 domains
class Route53DomainTagger(AwsResourceTagger):
    def add_tags(self):
        print(f"Tagging Route53 domain: {self.resource_id} in region {self.region}")
        route53domains = boto3.client('route53domains', region_name=self.region)
        try:
            route53domains.update_tags_for_domain(DomainName=[self.resource_id], TagsToUpdate=self.tags)
        except Exception as e:
            print(f"Error tagging Route53 domain {self.resource_id}: {e}")