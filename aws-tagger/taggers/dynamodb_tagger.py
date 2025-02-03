import boto3
from .base import AwsResourceTagger
from .registry import TaggerRegistry
from utils.arn_parser import AWSArnParser

# Concrete class for tagging ECS Resources
@TaggerRegistry.register("dynamodb")
class DynamoDBTagger(AwsResourceTagger):
    @staticmethod
    def tag_resource(arn: str, tags: list):
        region = AWSArnParser.get_region(arn)
        dynamo = boto3.client('dynamodb', region_name=region)
        try:
            dynamo.tag_resource(ResourceArn=arn, Tags=tags)
        except Exception as e:
            print(f"Error tagging {arn}: {e}")