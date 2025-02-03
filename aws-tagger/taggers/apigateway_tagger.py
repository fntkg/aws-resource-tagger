import boto3
from .base import AwsResourceTagger
from .registry import TaggerRegistry
from utils.tag_formatter import adapt_tags

# Concrete class for tagging Api Gateway
@TaggerRegistry.register("apigateway")
class ApiGatewayTagger(AwsResourceTagger):
    def __init__(self, region: str):
        self.apigateway = boto3.client('apigatewayv2', region_name=region)

    def tag_resource(self, arn: str, tags: list):
        try:
            self.apigateway.tag_resource(ResourceArn=arn, Tags=adapt_tags(tags))
        except Exception as e:
            print(f"Error tagging {arn}: {e}")