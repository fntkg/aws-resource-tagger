import boto3
from .base import AwsResourceTagger
from .registry import TaggerRegistry

# Concrete class for tagging ACM Certificates
@TaggerRegistry.register("acm")
class ACMTagger(AwsResourceTagger):
    def __init__(self, region: str):
        self.acm = boto3.client('acm', region_name=region)

    def tag_resource(self, arn: str, tags: list):
        try:
            self.acm.add_tags_to_certificate(CertificateArn=arn, Tags=tags)
        except Exception as e:
            print(f"Error tagging {arn}: {e}")