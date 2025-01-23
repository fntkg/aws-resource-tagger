import boto3
from .base_tagger import AwsResourceTagger
from utils.tag_formatter import adapt_autoscaling_tags
from utils.id_formatter import extract_resource_name

# Concrete class for tagging Autoscaling Groups
class AutoscalingGroupsTagger(AwsResourceTagger):
    def add_tags(self):
        print(f"Tagging Autoscaling Group: {self.resource_arn} in region {self.region}")
        resource_id = extract_resource_name(self.resource_arn)
        self.tags = adapt_autoscaling_tags(self.tags, resource_id)
        autoscaling = boto3.client('autoscaling', region_name=self.region)
        try:
            autoscaling.create_or_update_tags(Tags=self.tags)
        except Exception as e:
            print(f"Error tagging Autoscaling Group {self.resource_arn}: {e}")