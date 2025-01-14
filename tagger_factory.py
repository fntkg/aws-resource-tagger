from taggers.security_group_tagger import SecurityGroupTagger
from taggers.subnet_tagger import SubnetTagger
from taggers.route_table_tagger import RouteTableTagger
from taggers.sns_tagger import SimpleNotificationServiceTagger
from taggers.sqs_tagger import SimpleQueueServiceTagger
from taggers.ec2_volume_tagger import Ec2VolumeTagger
from taggers.ec2_unencrypted_snapshot_tagger import Ec2UnencryptedSnapshotTagger

# Factory class to create taggers based on resource type
class AwsResourceTaggerFactory:
    @staticmethod
    def get_tagger(resource_type, resource_id, tags, region):
        if resource_type == "securityGroup":
            return SecurityGroupTagger(resource_id, tags, region)
        elif resource_type == "subnet":
            return SubnetTagger(resource_id, tags, region)
        elif resource_type == "routeTable":
            return RouteTableTagger(resource_id, tags, region)
        elif resource_type == "sqs":
            return SimpleQueueServiceTagger(resource_id, tags, region)
        elif resource_type == "sns":
            return SimpleNotificationServiceTagger(resource_id, tags, region)
        elif resource_type == "volume":
            return Ec2VolumeTagger(resource_id, tags, region)
        elif resource_type == "ec2#unencryptedsnapshot":
            return Ec2UnencryptedSnapshotTagger(resource_id, tags, region)
        else:
            raise ValueError(f"Unsupported resource type: {resource_type}")