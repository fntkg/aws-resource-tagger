import boto3
from .base import AwsResourceTagger
from .registry import TaggerRegistry

# Concrete class for tagging RDS resources
@TaggerRegistry.register("rds")
class RdsTagger(AwsResourceTagger):
    def __init__(self, region: str):
        self.rds = boto3.client('rds', region_name=region)

    def tag_resource(self, arn: str, tags: list):
        try:
            self.rds.add_tags_to_resource(ResourceName=arn, Tags=tags)
        except Exception as e:
            print(f"Error tagging {arn}: {e}")