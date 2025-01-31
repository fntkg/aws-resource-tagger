import boto3
from .base import AwsResourceTagger
from utils.tag_formatter import adapt_ecs_tags
from .registry import TaggerRegistry
from arn_parser.arn_parser import AWSArnParser

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