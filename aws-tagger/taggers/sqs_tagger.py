import boto3
from .base import AwsResourceTagger
from .registry import TaggerRegistry
from arn_parser.arn_parser import AWSArnParser
from utils.tag_formatter import adapt_tags

# Concrete class for tagging SQS Queues\
@TaggerRegistry.register("sqs")
class SQSTagger(AwsResourceTagger):
    @staticmethod
    def tag_resource(arn: str, tags: list):
        print(f"Tagging SQS Queue: {arn}")
        region = AWSArnParser.get_region(arn)
        formated_tags = adapt_tags(tags)
        sqs = boto3.client('sqs', region_name=region)
        try:
            sqs.tag_queue(QueueUrl=arn, Tags=formated_tags)
        except Exception as e:
            print(f"Error tagging SQS Queue {arn}: {e}")