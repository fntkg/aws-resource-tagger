import boto3
from .base import AwsResourceTagger
from .registry import TaggerRegistry
from utils.arn_parser import AWSArnParser

# Concrete class for tagging EC2 Resources
@TaggerRegistry.register("ec2")
class EC2Tagger(AwsResourceTagger):
    @staticmethod
    def tag_resource(arn: str, tags: list):
        region = AWSArnParser.get_region(arn)
        resource_id = AWSArnParser.get_resource_id(arn)
        ec2 = boto3.client('ec2', region_name=region)
        try:
            ec2.create_tags(Resources=[resource_id], Tags=tags)
        except Exception as e:
            print(f"Error tagging {arn}: {e}")
