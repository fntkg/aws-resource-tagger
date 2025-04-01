import json
from tqdm import tqdm

from parsers.registry import ParserRegistry
from taggers.registry import TaggerRegistry
from utils.arn_parser import AWSArnParser


def load_tags(tags_file: str):
    """Load tags from a JSON file."""
    try:
        with open(tags_file, "r") as f:
            return json.load(f)
    except Exception as e:
        print(f"Error reading tags file: {e}")
        return None


def get_resources(input_file: str, parser_type: str):
    """Parse the input file to extract AWS resource ARNs."""
    parser = ParserRegistry.get_parser(parser_type)
    return parser.parse(input_file)


def tag_resource(arn: str, tags: list):
    """Tag a single AWS resource."""
    service = AWSArnParser.get_service(arn)
    region = AWSArnParser.get_region(arn)
    tagger = TaggerRegistry.get_tagger(service, region)
    tagger.tag_resource(arn, tags)


def tag_resources(input_file: str, tags_file: str, parser_type: str):
    """
    Parses an input file containing AWS resource ARNs and applies predefined tags to them.

    Args:
        input_file (str): Path to the file containing AWS resource ARNs.
        tags_file (str): Path to the file containing a list of dictionaries specifying the tags to be applied.
        parser_type (str): The type of parser to use for processing the input file.
    """
    tags = load_tags(tags_file)
    if tags is None:
        return

    resources = get_resources(input_file, parser_type)
    for arn in tqdm(resources):
        tag_resource(arn, tags)
