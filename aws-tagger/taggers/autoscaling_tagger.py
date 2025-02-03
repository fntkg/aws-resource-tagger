import boto3
from .base import AwsResourceTagger
from utils.tag_formatter import adapt_autoscaling_tags
from .registry import TaggerRegistry
from utils.arn_parser import AWSArnParser

# Concrete class for tagging Autoscaling Resources
@TaggerRegistry.register("autoscaling")
class AutoscalingTagger(AwsResourceTagger):
    @staticmethod
    def tag_resource(arn: str, tags: list):

        region = AWSArnParser.get_region(arn)
        resource_id = AWSArnParser.get_resource_id(arn)

        # The only supported value for resource_type is `auto-scaling-group`.
        formated_tags = adapt_autoscaling_tags(tags, resource_id, 'auto-scaling-group')

        autoscaling = boto3.client('autoscaling', region_name=region)
        try:
            autoscaling.create_or_update_tags(Tags=formated_tags)
        except Exception as e:
            print(f"Error tagging {arn}: {e}")