import boto3
from .base import AwsResourceTagger
from .registry import TaggerRegistry
from arn_parser.arn_parser import AWSArnParser

# Concrete class for tagging RDS resources
@TaggerRegistry.register("rds")
class RdsTagger(AwsResourceTagger):
    @staticmethod
    def tag_resource(arn: str, tags: list):
        region = AWSArnParser.get_region(arn)
        rds_snapshot = boto3.client('rds', region_name=region)
        try:
            rds_snapshot.add_tags_to_resource(ResourceName=arn, Tags=tags)
        except Exception as e:
            print(f"Error tagging {arn}: {e}")