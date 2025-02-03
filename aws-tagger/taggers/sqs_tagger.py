import boto3
from .base import AwsResourceTagger
from .registry import TaggerRegistry
from utils.tag_formatter import adapt_tags

# Concrete class for tagging SQS Queues\
@TaggerRegistry.register("sqs")
class SQSTagger(AwsResourceTagger):
    def __init__(self, region: str):
        self.sqs = boto3.client('sqs', region_name=region)

    def tag_resource(self, arn: str, tags: list):
        try:
            self.sqs.tag_queue(QueueUrl=arn, Tags=adapt_tags(tags))
        except Exception as e:
            print(f"Error tagging {arn}: {e}")