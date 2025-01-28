import boto3
from .base_tagger import AwsResourceTagger

# Concrete class for tagging Cloudwatch Alarms
class CloudWatchAlarmTagger(AwsResourceTagger):
    def add_tags(self):
        print(f"Tagging Cloudwatch Alarm: {self.resource_arn} in region {self.region}")
        alarm = boto3.client('cloudwatch', region_name=self.region)
        try:
            alarm.tag_resource(ResourceARN=self.resource_arn, Tags=self.tags)
        except Exception as e:
            print(f"Error tagging Cloudwatch Alarms {self.resource_arn}: {e}")