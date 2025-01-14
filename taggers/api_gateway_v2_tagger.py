import boto3
from .base_tagger import AwsResourceTagger
from utils.adapt_tag_sets import adapt_tags

# Concrete class for tagging Api Gateway v2
class ApiGatewayV2Tagger(AwsResourceTagger):
    def add_tags(self):
        print(f"Tagging Api Gateway v2: {self.resource_id} in region {self.region}")
        self.tags = adapt_tags(self.tags)
        apigateway = boto3.client('apigatewayv2', region_name=self.region)
        try:
            apigateway.tag_resource(ResourceArn=f'arn:aws:apigateway:{self.region}::/apis/{self.resource_id}', Tags=self.tags)
        except Exception as e:
            print(f"Error tagging Api Gateway v2 {self.resource_id}: {e}")