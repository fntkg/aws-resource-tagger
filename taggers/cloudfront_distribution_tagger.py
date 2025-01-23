import boto3
from .base_tagger import AwsResourceTagger

# Concrete class for tagging CloudFront Distributions
class CloudFrontDistributionTagger(AwsResourceTagger):
    def add_tags(self):
        print(f"Tagging CloudFront Distribution: {self.resource_arn} in region {self.region}")
        self.tags = {"Items": self.tags}
        cloudfront = boto3.client('cloudfront', region_name=self.region)
        try:
            cloudfront.tag_resource(Resource=f'{self.resource_arn}', Tags=self.tags)
        except Exception as e:
            print(f"Error tagging CloudFront Distribution {self.resource_arn}: {e}")