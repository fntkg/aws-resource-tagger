import boto3
from .base_tagger import AwsResourceTagger

# Concrete class for tagging SNS Topics
class SimpleNotificationServiceTagger(AwsResourceTagger):
    def add_tags(self):
        print(f"Tagging SNS Topic: {self.resource_arn} in region {self.region}")
        sns = boto3.client('sns', region_name=self.region)
        try:
            sns.tag_resource(ResourceArn=self.resource_arn, Tags=self.tags)
        except Exception as e:
            print(f"Error tagging SNS Topic {self.resource_arn}: {e}")