import boto3
from .base_tagger import AwsResourceTagger
from utils.csv_utils import get_s3_bucket_name

# Concrete class for tagging S3 buckets
class S3BucketTagger(AwsResourceTagger):
    def add_tags(self):
        self.resource_id = get_s3_bucket_name(self.resource_id)
        print(f"Tagging S3 bucket: {self.resource_id}")
        s3 = boto3.client('s3', region_name=self.region)
        try:
            s3.put_bucket_tagging(Bucket=self.resource_id, Tagging={'TagSet': self.tags})
        except Exception as e:
            print(f"Error tagging S3 bucket {self.resource_id}: {e}")