import boto3
from .base_tagger import AwsResourceTagger
from utils.tag_formatter import adapt_tags

# Concrete class for tagging CloudWatch Log Groups
class CloudWatchLogGroupTagger(AwsResourceTagger):
    def add_tags(self):
        self.tags = adapt_tags(self.tags) 
        print(f"CloudWatch Log Group: {self.resource_arn} in region {self.region}")
        logs = boto3.client('logs', region_name=self.region)
        try:
            logs.tag_resource(resourceArn=f'{self.resource_arn}', tags=self.tags)
        except Exception as e:
            print(f"Error tagging CloudWatch Log Group {self.resource_arn}: {e}")