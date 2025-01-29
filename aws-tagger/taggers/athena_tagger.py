import boto3
from .base import AwsResourceTagger
from .registry import TaggerRegistry
from arn_parser.arn_parser import AWSArnParser

# Concrete class for tagging Athena Resources
@TaggerRegistry.register("athena")
class AthenaTagger(AwsResourceTagger):
    @staticmethod
    def tag_resource(arn: str, tags: list):
        print(f"Tagging Athenas: {arn}")
        region = AWSArnParser.get_region(arn)
        athena = boto3.client('athena', region_name=region)
        try:
            athena.tag_resource(
                ResourceARN=arn,
                Tags=tags
            )
        except Exception as e:
            print(f"Error tagging Athena {arn}: {e}")