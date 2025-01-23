import boto3
from .base_tagger import AwsResourceTagger
from utils.id_formatter import extract_resource_name

# Concrete class for tagging EC2 Volumes
class Ec2VolumeTagger(AwsResourceTagger):
    def add_tags(self):
        print(f"Tagging EC2 Volume: {self.resource_arn} in region {self.region}")
        resource_id = extract_resource_name(self.resource_arn)
        ec2 = boto3.client('ec2', region_name=self.region)
        try:
            ec2.create_tags(Resources=[resource_id], Tags=self.tags)
        except Exception as e:
            print(f"Error tagging EC2 Volume {self.resource_arn}: {e}")