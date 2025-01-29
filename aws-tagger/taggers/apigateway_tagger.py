import boto3
from .base import AwsResourceTagger
from .registry import TaggerRegistry
from arn_parser.arn_parser import AWSArnParser
from utils.tag_formatter import adapt_tags

# Concrete class for tagging Api Gateway
@TaggerRegistry.register("apigateway")
class ApiGatewayTagger(AwsResourceTagger):
    @staticmethod
    def tag_resource(arn: str, tags: list):
        print(f"Tagging Api Gateway: {arn}")
        formated_tags = adapt_tags(tags)
        region = AWSArnParser.get_region(arn)
        apigateway = boto3.client('apigatewayv2', region_name=region)
        try:
            apigateway.tag_resource(ResourceArn=arn, Tags=formated_tags)
        except Exception as e:
            print(f"Error tagging Api Gateway {arn}: {e}")