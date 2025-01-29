import boto3
from .base import AwsResourceTagger
from .registry import TaggerRegistry
from arn_parser.arn_parser import AWSArnParser

# Concrete class for tagging CloudFront Resources
@TaggerRegistry.register("cloudfront")
class CloudfrontTagger(AwsResourceTagger):
    @staticmethod
    def tag_resource(arn: str, tags: list):
        print(f"Tagging CloudFront: {arn}")
        formated_tags = {"Items": tags}
        region = AWSArnParser.get_region(arn)
        cloudfront = boto3.client('cloudfront', region_name=region)
        try:
            cloudfront.tag_resource(Resource=f'{arn}', Tags=formated_tags)
        except Exception as e:
            print(f"Error tagging CloudFront Distribution {arn}: {e}")