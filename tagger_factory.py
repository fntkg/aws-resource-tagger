from taggers import (
    SecurityGroupTagger, SubnetTagger, RouteTableTagger, SimpleNotificationServiceTagger,
    SimpleQueueServiceTagger, Ec2VolumeTagger, Ec2UnencryptedSnapshotTagger, InternetGatewayTagger,
    NetworkAclTagger, VPCTagger, CloudFrontDistributionTagger, Route53DomainTagger,
    Route53HostedZoneTagger, ApiGatewayV2Tagger, AthenaWorkgroupTagger, AutoscalingGroupsTagger,
    RdsSnapshotTagger, S3BucketTagger, Ec2InstanceTagger, CloudWatchLogGroupTagger, ecr_tagger, lambda_tagger,
    ECSTagger, CloudWatchAlarmTagger
)


class AwsResourceTaggerFactory:
    """
    Factory class to create appropriate AWS resource taggers based on the provided resource type.

    Methods:
        get_tagger(resource_type, resource_arn, tags, region, account_id):
            Returns an instance of the appropriate tagger class based on the resource type.
    """

    @staticmethod
    def get_tagger(resource_type, resource_arn, tags, region, account_id):
        """
        Retrieves the appropriate AWS resource tagger instance.

        Args:
            resource_type (str): The type of AWS resource to be tagged.
            resource_arn (str): The unique identifier of the AWS resource.
            tags (list): A list of key-value pairs representing the tags to be applied.
            region (str): The AWS region where the resource is located.
            account_id (str): The AWS account ID associated with the resource.

        Returns:
            object: An instance of the corresponding resource tagger class.

        Raises:
            ValueError: If the provided resource type is not supported.

        The expected format for the `tags` parameter is:
        tags = [
            {"Key": "<tagkey>", "Value": "<tagvalue>"}
        ]
        """
        if resource_type == "securityGroup":
            return SecurityGroupTagger(resource_arn, tags, region)
        elif resource_type == "subnet":
            return SubnetTagger(resource_arn, tags, region)
        elif resource_type == "routetable":
            return RouteTableTagger(resource_arn, tags, region)
        elif resource_type == "sqs":
            return SimpleQueueServiceTagger(resource_arn, tags, region)
        elif resource_type == "sns":
            return SimpleNotificationServiceTagger(resource_arn, tags, region)
        elif resource_type == "volume":
            return Ec2VolumeTagger(resource_arn, tags, region)
        elif resource_type == "ec2#unencryptedsnapshot":
            return Ec2UnencryptedSnapshotTagger(resource_arn, tags, region)
        elif resource_type == "internetGateway":
            return InternetGatewayTagger(resource_arn, tags, region)
        elif resource_type == "networkAcl":
            return NetworkAclTagger(resource_arn, tags, region)
        elif resource_type == "vpc":
            return VPCTagger(resource_arn, tags, region)
        elif resource_type == "cloudfront":
            return CloudFrontDistributionTagger(resource_arn, tags, region, account_id)
        elif resource_type == "domain":
            return Route53DomainTagger(resource_arn, tags, region)
        elif resource_type == "dnsZone":
            return Route53HostedZoneTagger(resource_arn, tags, region)
        elif resource_type == "apiGatewayv2":
            return ApiGatewayV2Tagger(resource_arn, tags, region)
        elif resource_type == "athena#workgroup":
            return AthenaWorkgroupTagger(resource_arn, tags, region, account_id)
        elif resource_type == "autoScalingGroup":
            return AutoscalingGroupsTagger(resource_arn, tags, region, account_id)
        elif resource_type == "rds#snapshot" or resource_type == "rds/PostgreSQL/instance":
            return RdsSnapshotTagger(resource_arn, tags, region)
        elif resource_type == "bucket":
            return S3BucketTagger(resource_arn, tags)
        elif resource_type == "virtualMachine":
            return Ec2InstanceTagger(resource_arn, tags, region)
        elif resource_type == "logs#loggroup":
            return CloudWatchLogGroupTagger(resource_arn, tags, region)
        elif resource_type == "repository":
            return ecr_tagger.ECRRepositoryTagger(resource_arn, tags, region)
        elif resource_type == "lambda":
            return lambda_tagger.LambdaTagger(resource_arn, tags, region)
        elif resource_type == "ecs#service" or resource_type == "task":
            return ECSTagger(resource_arn, tags, region)
        elif resource_type == "metricfilteralarm":
            return CloudWatchAlarmTagger(resource_arn, tags, region)
        else:
            raise ValueError(f"Unsupported resource type: {resource_type}")
