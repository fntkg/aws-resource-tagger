import boto3
from .base import AwsResourceTagger
from .registry import TaggerRegistry
from arn_parser.arn_parser import AWSArnParser

# Concrete class for tagging ACM Certificates
@TaggerRegistry.register("acm")
class ACMTagger(AwsResourceTagger):
    @staticmethod
    def tag_resource(arn: str, tags: list):
        print(f"Tagging ACM Certificate: {arn}")
        region = AWSArnParser.get_region(arn)
        certificate = boto3.client('acm', region_name=region)
        try:
            certificate.add_tags_to_certificate(CertificateArn=arn, Tags=tags)
        except Exception as e:
            print(f"Error tagging ACM Certificate {arn}: {e}")