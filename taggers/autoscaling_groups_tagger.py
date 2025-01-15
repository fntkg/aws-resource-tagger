import boto3
from .base_tagger import AwsResourceTagger
from utils.adapt_tag_sets import adapt_autoscaling_tags

# Concrete class for tagging Autoscaling Groups
class AutoscalingGroupsTagger(AwsResourceTagger):
    def add_tags(self):
        print(f"Tagging Autoscaling Group: {self.resource_id} in region {self.region}")
        self.tags = adapt_autoscaling_tags(self.tags, self.resource_id)
        autoscaling = boto3.client('autoscaling', region_name=self.region)
        try:
            autoscaling.create_or_update_tags(Tags=self.tags)
        except Exception as e:
            print(f"Error tagging Autoscaling Group {self.resource_id}: {e}")