import boto3
from .base import AwsResourceTagger
from utils.tag_formatter import adapt_tags
from .registry import TaggerRegistry
from utils.arn_parser import AWSArnParser

# Concrete class for tagging Lambda resources
@TaggerRegistry.register("lambda")
class LambdaTagger(AwsResourceTagger):
    @staticmethod
    def tag_resource(arn: str, tags: list):
        formated_tags = adapt_tags(tags)
        region = AWSArnParser.get_region(arn)
        function = boto3.client('lambda', region_name=region)
        try:
            function.tag_resource(Resource=arn, Tags=formated_tags)
        except Exception as e:
            print(f"Error tagging {arn}: {e}")