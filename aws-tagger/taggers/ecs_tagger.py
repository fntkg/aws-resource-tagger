import boto3
from .base import AwsResourceTagger
from utils.tag_formatter import adapt_ecs_tags
from .registry import TaggerRegistry

# Concrete class for tagging ECS Resources
@TaggerRegistry.register("ecs")
class ECSTagger(AwsResourceTagger):
    def __init__(self, region: str):
        self.ecs = boto3.client('ecs', region_name=region)

    def tag_resource(self, arn: str, tags: list):
        try:
            self.ecs.tag_resource(resourceArn=arn, tags=adapt_ecs_tags(tags))
        except Exception as e:
            print(f"Error tagging {arn}: {e}")