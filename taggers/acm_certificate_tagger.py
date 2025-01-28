import boto3
from .base_tagger import AwsResourceTagger

# Concrete class for tagging ACM Certificates
class ACMCertificateTagger(AwsResourceTagger):
    def add_tags(self):
        print(f"Tagging ACM Certificate: {self.resource_arn} in region {self.region}")
        certificate = boto3.client('acm', region_name=self.region)
        try:
            certificate.add_tags_to_certificate(CertificateArn=self.resource_arn, Tags=self.tags)
        except Exception as e:
            print(f"Error tagging ACM Certificate {self.resource_arn}: {e}")