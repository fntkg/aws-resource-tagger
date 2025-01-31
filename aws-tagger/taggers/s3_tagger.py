import boto3
from .base import AwsResourceTagger
from .registry import TaggerRegistry
from arn_parser.arn_parser import AWSArnParser

# Concrete class for tagging S3 resources
@TaggerRegistry.register("s3")
class S3Tagger(AwsResourceTagger):
    @staticmethod
    def tag_resource(arn: str, tags: list):
        region = AWSArnParser.get_region(arn)
        resource_id = AWSArnParser.get_resource_id(arn)
        s3 = boto3.client('s3', region_name=region)
        try:
            s3.put_bucket_tagging(Bucket=resource_id, Tagging={'TagSet': tags})
        except Exception as e:
            print(f"Error tagging {arn}: {e}")