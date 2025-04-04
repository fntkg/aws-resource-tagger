def adapt_tags(tags):
    """
    Adapt a list of dictionaries to a single dictionary format.

    Args:
        tags (list): List of dictionaries with 'Key' and 'Value'.

    Returns:
        dict: Dictionary with keys and values from the input list.
    """
    return {tag['Key']: tag['Value'] for tag in tags}

def adapt_autoscaling_tags(tags, resource_id, resource_type='auto-scaling-group'):
    """
    Transforms a list of tag dictionaries into the desired format.

    :param tags: List of dictionaries with 'Key' and 'Value' keys.
    :param resource_id: Resource identifier to include in each tag.
    :param resource_type: Resource type to include in each tag (default: 'auto-scaling-group').
    :return: List of transformed dictionaries.
    """
    return [
        {
            'Key': tag['Key'],
            'Value': tag['Value'],
            'PropagateAtLaunch': True,
            'ResourceId': resource_id,
            'ResourceType': resource_type
        }
        for tag in tags
    ]

def adapt_ecs_tags(tags):
    """
    Adapt a list of dictionaries to a single dictionary format for ECS resources.

    Args:
        tags (list): List of dictionaries with 'Key' and 'Value'.

    Returns:
        dict: Dictionary with keys and values from the input list.
    """
    return [{'key': tag['Key'],'value': tag['Value']} for tag in tags]