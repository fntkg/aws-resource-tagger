import boto3
from .base_tagger import AwsResourceTagger
from utils.tag_formatter import adapt_tags

# Concrete class for tagging Api Gateway v2
class ApiGatewayV2Tagger(AwsResourceTagger):
    def add_tags(self):
        print(f"Tagging Api Gateway v2: {self.resource_arn} in region {self.region}")
        self.tags = adapt_tags(self.tags)
        apigateway = boto3.client('apigatewayv2', region_name=self.region)
        try:
            apigateway.tag_resource(ResourceArn=f'{self.resource_arn}', Tags=self.tags)
        except Exception as e:
            print(f"Error tagging Api Gateway v2 {self.resource_arn}: {e}")