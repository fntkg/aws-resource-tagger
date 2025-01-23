def extract_resource_name(arn):
    """
    Extracts the resource name from an AWS ARN.

    Args:
        arn (str): The ARN string from which to extract the resource name.

    Returns:
        str: The extracted resource name.
    """
    return arn.split('/')[-1]