import boto3
from .base import AwsResourceTagger
from .registry import TaggerRegistry


# Concrete class for tagging ECR resources
@TaggerRegistry.register("ecr")
class ECRTagger(AwsResourceTagger):
    def __init__(self, region: str):
        self.ecr = boto3.client('ecr', region_name=region)

    def tag_resource(self, arn: str, tags: list):
        try:
            self.ecr.tag_resource(resourceArn=arn, tags=tags)
        except Exception as e:
            print(f"Error tagging {arn}: {e}")
