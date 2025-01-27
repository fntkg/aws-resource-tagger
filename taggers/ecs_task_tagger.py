import boto3
from .base_tagger import AwsResourceTagger
from utils.tag_formatter import adapt_ecs_tags

# Concrete class for tagging ECS Resources
class ECSTagger(AwsResourceTagger):
    def add_tags(self):
        print(f"Tagging ECS Resource: {self.resource_arn} in region {self.region}")
        self.tags = adapt_ecs_tags(self.tags)
        task = boto3.client('ecs', region_name=self.region)
        try:
            task.tag_resource(resourceArn=self.resource_arn, tags=self.tags)
        except Exception as e:
            print(f"Error tagging ECS Resource {self.resource_arn}: {e}")