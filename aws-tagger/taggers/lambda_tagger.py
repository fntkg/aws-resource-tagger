import boto3
from .base import AwsResourceTagger
from utils.tag_formatter import adapt_tags
from .registry import TaggerRegistry

# Concrete class for tagging Lambda resources
@TaggerRegistry.register("lambda")
class LambdaTagger(AwsResourceTagger):
    def __init__(self, region: str):
        self.function = boto3.client('lambda', region_name=region)

    def tag_resource(self, arn: str, tags: list):
        try:
            self.function.tag_resource(Resource=arn, Tags=adapt_tags(tags))
        except Exception as e:
            print(f"Error tagging {arn}: {e}")