import boto3
from .base import AwsResourceTagger
from .registry import TaggerRegistry

# Concrete class for tagging SNS Resouces
@TaggerRegistry.register("sns")
class SNSTagger(AwsResourceTagger):
    def __init__(self, region: str):
        self.sns = boto3.client('sns', region_name=region)

    def tag_resource(self, arn: str, tags: list):
        try:
            self.sns.tag_resource(ResourceArn=arn, Tags=tags)
        except Exception as e:
            print(f"Error tagging {arn}: {e}")