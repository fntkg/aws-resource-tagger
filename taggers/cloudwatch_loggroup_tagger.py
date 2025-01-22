import boto3
from .base_tagger import AwsResourceTagger

# Concrete class for tagging CloudWatch Log Groups
class CloudWatchLogGroupTagger(AwsResourceTagger):
    def add_tags(self):
        print(f"CloudWatch Log Group: {self.resource_id} in region {self.region}")
        logs = boto3.client('logs', region_name=self.region)
        try:
            # Note that the tags must a dict not a list of dicts for the log group
            logs.tag_resource(resourceArn=self.full_resource_id, tags=self.tags)
        except Exception as e:
            print(f"Error tagging CloudWatch Log Group {self.resource_id}: {e}")