import boto3
from .base_tagger import AwsResourceTagger
from utils.id_formatter import extract_resource_name

# Concrete class for tagging Route53 domains
class Route53HostedZoneTagger(AwsResourceTagger):
    def add_tags(self):
        print(f"Tagging Route53 Hosted Zone: {self.resource_arn} in region {self.region}")
        resource_id = extract_resource_name(self.resource_arn)
        route53 = boto3.client('route53', region_name=self.region)
        try:
            route53.change_tags_for_resource(ResourceType='hostedzone', ResourceId=resource_id, AddTags=self.tags)
        except Exception as e:
            print(f"Error tagging Route53 Hosted Zone {self.resource_arn}: {e}")