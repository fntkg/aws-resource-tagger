import boto3
from .base_tagger import AwsResourceTagger

# Concrete class for tagging CloudFront Distributions
class CloudFrontDistributionTagger(AwsResourceTagger):
    def add_tags(self):
        print(f"Tagging CloudFront Distribution: {self.resource_id} in region {self.region}")
        self.tags = {"Items": self.tags}
        cloudfront = boto3.client('cloudfront', region_name=self.region)
        try:
            cloudfront.tag_resource(Resource=f'arn:aws:cloudfront::{self.account_id}:distribution/${self.resource_id}', Tags=self.tags)
        except Exception as e:
            print(f"Error tagging CloudFront Distribution {self.resource_id}: {e}")