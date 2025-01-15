from taggers.security_group_tagger import SecurityGroupTagger
from taggers.subnet_tagger import SubnetTagger
from taggers.route_table_tagger import RouteTableTagger
from taggers.sns_tagger import SimpleNotificationServiceTagger
from taggers.sqs_tagger import SimpleQueueServiceTagger
from taggers.ec2_volume_tagger import Ec2VolumeTagger
from taggers.ec2_unencrypted_snapshot_tagger import Ec2UnencryptedSnapshotTagger
from taggers.internet_gateway_tagger import InternetGatewayTagger
from taggers.network_acl_tagger import NetworkAclTagger
from taggers.vpc_tagger import VPCTagger
from taggers.cloudfront_distribution_tagger import CloudFrontDistributionTagger
from taggers.route53_domain_tagger import Route53DomainTagger
from taggers.route53_zone_tagger import Route53HostedZoneTagger
from taggers.api_gateway_v2_tagger import ApiGatewayV2Tagger
from taggers.athena_workgroup_tagger import AthenaWorkgroupTagger
from taggers.autoscaling_groups_tagger import AutoscalingGroupsTagger

# Factory class to create taggers based on resource type
class AwsResourceTaggerFactory:
    @staticmethod
    def get_tagger(resource_type, resource_id, tags, region, account_id):
        if resource_type == "securityGroup":
            return SecurityGroupTagger(resource_id, tags, region)
        elif resource_type == "subnet":
            return SubnetTagger(resource_id, tags, region)
        elif resource_type == "routetable":
            return RouteTableTagger(resource_id, tags, region)
        elif resource_type == "sqs":
            return SimpleQueueServiceTagger(resource_id, tags, region)
        elif resource_type == "sns":
            return SimpleNotificationServiceTagger(resource_id, tags, region)
        elif resource_type == "volume":
            return Ec2VolumeTagger(resource_id, tags, region)
        elif resource_type == "ec2#unencryptedsnapshot":
            return Ec2UnencryptedSnapshotTagger(resource_id, tags, region)
        elif resource_type == "internetGateway":
            return InternetGatewayTagger(resource_id, tags, region)
        elif resource_type == "networkAcl":
            return NetworkAclTagger(resource_id, tags, region)
        elif resource_type == "vpc":
            return VPCTagger(resource_id, tags, region)
        elif resource_type == "cloudfront":
            return CloudFrontDistributionTagger(resource_id, tags, region, account_id)
        elif resource_type == "domain":
            return Route53DomainTagger(resource_id, tags, region)
        elif resource_type == "dnsZone":
            return Route53HostedZoneTagger(resource_id, tags, region)
        elif resource_type == "apiGatewayv2":
            return ApiGatewayV2Tagger(resource_id, tags, region)
        elif resource_type == "athena#workgroup":
            return AthenaWorkgroupTagger(resource_id, tags, region, account_id)
        elif resource_type == "autoScalingGroup":
            return AutoscalingGroupsTagger(resource_id, tags, region, account_id)
        else:
            raise ValueError(f"Unsupported resource type: {resource_type}")