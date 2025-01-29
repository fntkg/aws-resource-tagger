import boto3
from .base import AwsResourceTagger
from utils.tag_formatter import adapt_ecs_tags
from .registry import TaggerRegistry
from arn_parser.arn_parser import AWSArnParser

# Concrete class for tagging ECS Resources
@TaggerRegistry.register("ecs")
class ECSTagger(AwsResourceTagger):
    def tag_resource(arn: str, tags: list):
        print(f"Tagging ECS Resource: {arn}")
        formated_tags = adapt_ecs_tags(tags)
        region = AWSArnParser.get_region(arn)
        task = boto3.client('ecs', region_name=region)
        try:
            task.tag_resource(resourceArn=arn, tags=formated_tags)
        except Exception as e:
            print(f"Error tagging ECS Resource {arn}: {e}")