import boto3
from .base import AwsResourceTagger
from .registry import TaggerRegistry
from arn_parser.arn_parser import AWSArnParser

# Concrete class for tagging ECR resources
@TaggerRegistry.register("ecr")
class ECRTagger(AwsResourceTagger):
    @staticmethod
    def tag_resource(arn: str, tags: list):
        print(f"Tagging ECR: {arn}")
        region = AWSArnParser.get_region(arn)
        ecr = boto3.client('ecr', region_name=region)
        try:
            ecr.tag_resource(resourceArn=arn, tags=tags)
        except Exception as e:
            print(f"Error tagging ECR Repository {arn}: {e}")