import boto3
from .base import AwsResourceTagger
from utils.tag_formatter import adapt_autoscaling_tags
from .registry import TaggerRegistry
from utils.arn_parser import AWSArnParser

# Concrete class for tagging Autoscaling Resources
@TaggerRegistry.register("autoscaling")
class AutoscalingTagger(AwsResourceTagger):
    def __init__(self, region: str):
        self.autoscaling = boto3.client('autoscaling', region_name=region)

    def tag_resource(self, arn: str, tags: list):
        # The only supported value for resource_type is `auto-scaling-group`.
        try:
            self.autoscaling.create_or_update_tags(
                Tags=adapt_autoscaling_tags(tags, AWSArnParser.get_resource_id(arn),
                                            'auto-scaling-group')
            )
        except Exception as e:
            print(f"Error tagging {arn}: {e}")