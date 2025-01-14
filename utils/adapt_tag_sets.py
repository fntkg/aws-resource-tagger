def adapt_tags(input_tags):
    """
    Adapt a list of dictionaries to a single dictionary format.

    Args:
        input_tags (list): List of dictionaries with 'Key' and 'Value'.

    Returns:
        dict: Dictionary with keys and values from the input list.
    """
    return {tag['Key']: tag['Value'] for tag in input_tags}