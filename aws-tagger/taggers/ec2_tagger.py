import boto3
from .base import AwsResourceTagger
from .registry import TaggerRegistry
from utils.arn_parser import AWSArnParser

# Concrete class for tagging EC2 Resources
@TaggerRegistry.register("ec2")
class EC2Tagger(AwsResourceTagger):
    def __init__(self, region: str):
        self.ec2 = boto3.client('ec2', region_name=region)

    def tag_resource(self, arn: str, tags: list):
        try:
            self.ec2.create_tags(Resources=[AWSArnParser.get_resource_id(arn)], Tags=tags)
        except Exception as e:
            print(f"Error tagging {arn}: {e}")
