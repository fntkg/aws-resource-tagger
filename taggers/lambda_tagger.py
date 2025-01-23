import boto3
from .base_tagger import AwsResourceTagger
from utils.tag_formatter import adapt_tags
from utils.id_formatter import extract_resource_name

# Concrete class for tagging Lambda functions
class LambdaTagger(AwsResourceTagger):
    def add_tags(self):
        print(f"Tagging Lambda function: {self.resource_arn} in region {self.region}")
        resource_id = extract_resource_name(self.resource_arn)
        self.tags = adapt_tags(self.tags)
        function = boto3.client('lambda', region_name=self.region)
        try:
            function.tag_resource(Resource=resource_id, Tags=self.tags)
        except Exception as e:
            print(f"Error tagging Lambda function {self.resource_arn}: {e}")