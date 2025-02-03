import boto3
from .base import AwsResourceTagger
from .registry import TaggerRegistry

# Concrete class for tagging CloudFront Resources
@TaggerRegistry.register("cloudfront")
class CloudfrontTagger(AwsResourceTagger):
    def __init__(self, region: str):
        self.cloudfront = boto3.client('cloudfront', region_name=region)

    def tag_resource(self, arn: str, tags: list):
        try:
            self.cloudfront.tag_resource(Resource=f'{arn}', Tags={"Items": tags})
        except Exception as e:
            print(f"Error tagging {arn}: {e}")