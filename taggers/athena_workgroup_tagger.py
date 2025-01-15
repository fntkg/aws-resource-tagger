import boto3
from .base_tagger import AwsResourceTagger

# Concrete class for tagging Athena Workgroups
class AthenaWorkgroupTagger(AwsResourceTagger):
    def add_tags(self):
        print(f"Tagging Athena Workgroup: {self.resource_id} in region {self.region}")
        athena = boto3.client('athena', region_name=self.region)
        try:
            athena.tag_resource(
                ResourceARN=f'arn:aws:athena:{self.region}:{self.account_id}:workgroup/{self.resource_id}',
                Tags=self.tags
            )
        except Exception as e:
            print(f"Error tagging Athena Workgroup {self.resource_id}: {e}")