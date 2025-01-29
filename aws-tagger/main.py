import typer
from cli import tag_resources

# Initialize a Typer application
app = typer.Typer()

@app.command()
def tag(
    input_file: str = typer.Argument(help="Path to the input file containing AWS resource ARNs."),
    tags_file: str = typer.Argument(
        help="Path to the file containing a list of tags_file to apply, provided in JSON format. "
             "(e.g., [{Key:Environment,Value:Production}])"),
    parser_type: str = typer.Option("wiz", "--parser", help="Type of parser to use (e.g., csv, json)."),
):
    """
    Tags AWS resources based on an input file.

    Args:
        input_file (str): Path to the file with AWS resource ARNs.
        tags_file (list): Tags to apply, provided in JSON format (e.g., '[{"Key": "Environment", "Value": "Production"}]').
        parser_type (str): Type of parser used for processing the file (default: "wiz").

    Example Usage:
        ```sh
        python main.py tag resources.csv '[{"Key": "Environment", "Value": "Production"}]' --parser csv
        ```

    Notes:
        - The `parser_type` should be registered in the application's parser registry.
        - Ensure the tags_file are properly formatted JSON strings.
    """
    tag_resources(input_file, tags_file, parser_type)

if __name__ == "__main__":
    app()
