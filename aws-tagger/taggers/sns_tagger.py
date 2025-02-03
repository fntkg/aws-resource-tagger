import boto3
from .base import AwsResourceTagger
from .registry import TaggerRegistry
from utils.arn_parser import AWSArnParser

# Concrete class for tagging SNS Resouces
@TaggerRegistry.register("sns")
class SNSTagger(AwsResourceTagger):
    @staticmethod
    def tag_resource(arn: str, tags: list):
        region = AWSArnParser.get_region(arn)
        sns = boto3.client('sns', region_name=region)
        try:
            sns.tag_resource(ResourceArn=arn, Tags=tags)
        except Exception as e:
            print(f"Error tagging {arn}: {e}")