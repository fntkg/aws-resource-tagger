# AWS Resource Tagging Tool

This tool allows you to easily tag any AWS resource in your account. It simplifies the process of applying tags to multiple resources across AWS services, making it especially useful for managing and organizing your infrastructure at scale.

## Features

- **Tag Resources Easily**: Apply tags to any AWS resource by simply providing a list of resources and the tags to be applied.
- **Support for Multiple Input Formats**: Handle different input formats, such as CSV files, ARNs, and others, by using custom parsers.
- **Extendable**: Add your own parsers and taggers with minimal effort.
- **Automated Resource Identification**: The tool automatically identifies the AWS service, region, account ID, and resource name from ARNs.

## Installation

To install the project and its dependencies, simply run:

```bash
pip install -r requirements.txt
```

## Usage

### Tagging Resources

To tag AWS resources, you need to pass a list of resources and tags to the script. You can provide the resources in a variety of formats, such as a CSV file or a plain ARN list. Additionally, you can specify the tags in a JSON file for simplicity.

**Example**: Tagging resources from a CSV file:

```bash
python main.py tag resources.csv tags.json --parser csv
```

Where:

- `resources.csv` is a file containing the list of resources to be tagged.
- `tags.json` is a file containing the tags to be applied, in the following format:

```json
[
  {
    "Key": "Environment",
    "Value": "Production"
  },
  {
    "Key": "Department",
    "Value": "DevOps"
  }
]
```

### Supported Parsers

- **WIZ generated CSV Parser**: Handles CSV files generated by WIZ.
- You can easily add your own custom parsers by creating a new class that follows the interface pattern.

### Adding Custom Parsers and Taggers

This tool is designed to be extensible. Adding your own parsers and taggers is straightforward:

1. **Custom Parsers**: Create a class that implements the Parser interface. Your parser class should have a method to read the input file and return a list of AWS resources (ARNs).
2. **Custom Taggers**: Create a class that implements the Tagger interface. Your tagger class should handle the logic to apply tags to the resources.

Once created, simply register your parser or tagger with the tool, and it will be available for use.

**Example**: Creating a custom parser for a new input format:

```python
from .base import BaseParser
from .registry import ParserRegistry

@register_parser('custom') # Register the parser with the tool
class CustomParser(Parser):
    @staticmethod
    def parse(input_file: str) -> list:
        resources = [] # List of resources (ARNs)
        # Your logic to read the input file and extract resources
        return resources
```

**Example**: Creating a custom tager for a new AWS service:

```python
import boto3
from .base import AwsResourceTagger
from .registry import TaggerRegistry
from arn_parser.arn_parser import AWSArnParser

@TaggerRegistry.register("yourservice") # Register the tagger with the tool. This is the service name.
class YourServiceTagger(AwsResourceTagger):
    @staticmethod
    def tag_resource(arn: str, tags: list):
        # Your logic to tag the resource
```

### Example Command

Here’s how you can tag AWS resources using a CSV file and a custom set of tags:

```bash
python main.py tag resources.csv tags.json --parser csv
```

- `resources.csv`: A file containing AWS resources (ARNs) to be tagged.
- `tags.json`: A JSON file containing the tags in the expected format.
- `--parser csv`: Specifies the parser to use for processing the input file (in this case, CSV format).

## Contributing

We encourage contributions to this project! If you have ideas for new parsers, taggers, or other improvements, feel free to submit a pull request.

### How to Contribute

1. Fork the repository.
2. Create a new branch for your feature (git checkout -b feature-name).
3. Make your changes and commit them (git commit -am 'Add new feature').
4. Push to the branch (git push origin feature-name).
5. Open a pull request.

### Adding Custom Parsers or Taggers

1. Create a new Python file inside the parsers or taggers directory.
2. Define a class that implements the appropriate interface (Parser or Tagger).
3. Register your class using the register_parser or register_tagger function, as appropriate.

## About how I designed this

This project employs several design patterns to ensure flexibility, extensibility, and maintainability:

- **Factory Pattern**: Used for the dynamic creation of parsers and taggers based on user input. This allows the system to easily accommodate new types of parsers and taggers without changing the core logic.
- **Decorator Pattern**: Applied to register parsers and taggers, simplifying the extension of functionality with minimal boilerplate code.
- **Strategy Pattern**: Defines different parsing and tagging strategies (such as tagging EC2, S3, etc.), which can be easily switched and customized based on the resource type.
- **Singleton Pattern**: Ensures only one instance of each parser and tagger registries exists, preventing duplication and ensuring consistent behavior across the system.

These patterns work together to keep the project modular, maintainable, and easy to extend for future requirements.