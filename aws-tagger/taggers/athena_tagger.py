import boto3
from .base import AwsResourceTagger
from .registry import TaggerRegistry

# Concrete class for tagging Athena Resources
@TaggerRegistry.register("athena")
class AthenaTagger(AwsResourceTagger):
    def __init__(self, region: str):
        self.athena = boto3.client('athena', region_name=region)

    def tag_resource(self, arn: str, tags: list):
        try:
            self.athena.tag_resource(
                ResourceARN=arn,
                Tags=tags
            )
        except Exception as e:
            print(f"Error tagging {arn}: {e}")