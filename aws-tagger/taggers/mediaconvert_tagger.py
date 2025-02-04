import boto3
from .base import AwsResourceTagger
from .registry import TaggerRegistry
from utils.tag_formatter import adapt_tags


# Concrete class for tagging Elemental Media Convert
@TaggerRegistry.register("mediaconvert")
class MediaConvertTagger(AwsResourceTagger):
    def __init__(self, region: str):
        self.client = boto3.client('mediaconvert', region_name=region)

    def tag_resource(self, arn: str, tags: list):
        try:
            formated_tags = adapt_tags(tags)
            self.client.tag_resource(Arn=arn, Tags=formated_tags)
        except Exception as e:
            print(f"Error tagging {arn}: {e}")
