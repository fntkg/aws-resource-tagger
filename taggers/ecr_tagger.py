import boto3
from .base_tagger import AwsResourceTagger

# Concrete class for tagging ECR Repositories
class ECRRepositoryTagger(AwsResourceTagger):
    def add_tags(self):
        print(f"Tagging ECR Repository: {self.resource_arn} in region {self.region}")
        ecr = boto3.client('ecr', region_name=self.region)
        try:
            ecr.tag_resource(resourceArn=self.resource_arn, tags=self.tags)
        except Exception as e:
            print(f"Error tagging ECR Repository {self.resource_arn}: {e}")