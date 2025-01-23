import boto3
from .base_tagger import AwsResourceTagger

# Concrete class for tagging RDS Snapshots
class RdsSnapshotTagger(AwsResourceTagger):
    def add_tags(self):
        print(f"Tagging RDS Snapshot: {self.resource_arn} in region {self.region}")
        rds_snapshot = boto3.client('rds', region_name=self.region)
        try:
            rds_snapshot.add_tags_to_resource(ResourceName=self.resource_arn, Tags=self.tags)
        except Exception as e:
            print(f"Error tagging RDS Snapshot {self.resource_arn}: {e}")