import boto3
from .base import AwsResourceTagger
from .registry import TaggerRegistry
from utils.arn_parser import AWSArnParser

# Concrete class for tagging S3 resources
@TaggerRegistry.register("s3")
class S3Tagger(AwsResourceTagger):
    def __init__(self, region: str):
        self.s3 = boto3.client('s3', region_name=region)

    def tag_resource(self, arn: str, tags: list):
        try:
            self.s3.put_bucket_tagging(Bucket=AWSArnParser.get_resource_id(arn), Tagging={'TagSet': tags})
        except Exception as e:
            print(f"Error tagging {arn}: {e}")