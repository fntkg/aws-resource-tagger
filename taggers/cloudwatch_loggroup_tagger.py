import boto3
from .base_tagger import AwsResourceTagger
from utils.adapt_tag_sets import adapt_tags

# Concrete class for tagging CloudWatch Log Groups
class CloudWatchLogGroupTagger(AwsResourceTagger):
    def add_tags(self):
        self.tags = adapt_tags(self.tags) 
        print(f"CloudWatch Log Group: {self.full_resource_id} in region {self.region}")
        logs = boto3.client('logs', region_name=self.region)
        try:
            logs.tag_resource(resourceArn=self.full_resource_id, tags=self.tags)
        except Exception as e:
            print(f"Error tagging CloudWatch Log Group {self.resource_id}: {e}")