import boto3
from .base import AwsResourceTagger
from .registry import TaggerRegistry

# Concrete class for tagging ECS Resources
@TaggerRegistry.register("dynamodb")
class DynamoDBTagger(AwsResourceTagger):
    def __init__(self, region: str):
        self.dynamodb = boto3.client('dynamodb', region_name=region)

    def tag_resource(self, arn: str, tags: list):
        try:
            self.dynamodb.tag_resource(ResourceArn=arn, Tags=tags)
        except Exception as e:
            print(f"Error tagging {arn}: {e}")