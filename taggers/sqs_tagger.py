import boto3
from .base_tagger import AwsResourceTagger

# Concrete class for tagging SQS Queues
class SimpleQueueServiceTagger(AwsResourceTagger):
    def add_tags(self):
        print(f"Tagging SQS Queue: {self.resource_id} in region {self.region}")
        sqs = boto3.client('sqs', region_name=self.region)
        try:
            sqs.tag_queue(QueueUrl=self.resource_id, Tags={tag['Key']: tag['Value'] for tag in self.tags})
        except Exception as e:
            print(f"Error tagging SQS Queue {self.resource_id}: {e}")