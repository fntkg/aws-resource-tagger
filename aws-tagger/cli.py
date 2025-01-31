from parsers.registry import ParserRegistry
import parsers
import taggers
from tqdm import tqdm
import json
from taggers.registry import TaggerRegistry
from arn_parser.arn_parser import AWSArnParser


def tag_resources(input_file: str, tags_file: str, parser_type: str):
    """
    Parses an input file containing AWS resource ARNs and applies predefined tags_file to them.

    Args:
        input_file (str): Path to the file containing AWS resource ARNs.
        tags_file (list): Path to the file containing a list of dictionaries specifying the tags_file to be applied.
                     Example: [{"Key": "Environment", "Value": "Development"}]
        parser_type (str): The type of parser to use for processing the input file.
                           Must be registered in `ParserRegistry`.

    Example:
        tag_resources("resources.csv", [{"Key": "Project", "Value": "Alpha"}], "wiz")

    Output:
        Prints the number of successfully tagged resources.
    """
    # Leer los tags_file desde el archivo JSON
    try:
        with open(tags_file, "r") as f:
            tags = json.load(f)
    except Exception as e:
        print(f"Error reading tags_file file: {e}")
        return
    # Get the parser instance based on the parser type
    parser = ParserRegistry.get_parser(parser_type)

    # Extract AWS resource ARNs from the input file
    resources = parser.parse(input_file)

    for arn in tqdm(resources):
        # Determine the AWS service from the ARN
        service = AWSArnParser.get_service(arn)

        # Retrieve the appropriate tagger for the AWS service
        tagger = TaggerRegistry.get_tagger(service)

        # Apply the predefined tags to the resource
        tagger.tag_resource(arn, tags)