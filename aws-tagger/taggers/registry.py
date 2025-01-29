from .base import AwsResourceTagger

class TaggerRegistry:
    """
    A registry for managing AWS resource taggers.

    This class allows dynamic registration and retrieval of taggers responsible for
    tagging different types of AWS resources. It follows the **Registry Pattern**
    to ensure that taggers can be registered and retrieved efficiently.

    Attributes:
        _taggers (dict): A dictionary mapping resource types (str) to their respective
                         tagger classes.
    """

    _taggers = {}

    @classmethod
    def register(cls, name: str) -> callable:
        """
        A decorator to register a tagger class under a specified resource type.

        Args:
            name (str): The AWS resource type to associate with the tagger class.

        Returns:
            callable: The decorator function that registers the class.

        Example:
            ```python
            @TaggerRegistry.register("ec2")
            class EC2Tagger(AwsResourceTagger):
                ...
            ```
        """
        def wrapper(tagger_class):
            cls._taggers[name] = tagger_class
            return tagger_class
        return wrapper

    @classmethod
    def get_tagger(cls, resource_type: str) -> AwsResourceTagger:
        """
        Retrieves the tagger class for a given AWS resource type.

        Args:
            resource_type (str): The type of AWS resource (e.g., "ec2", "s3").

        Returns:
            AwsResourceTagger: An instance of the registered tagger class.

        Raises:
            ValueError: If no tagger is registered for the given resource type.

        Example:
            ```python
            tagger = TaggerRegistry.get_tagger("ec2")
            tagger.tag_resource(arn, tags_file)
            ```
        """
        tagger_cls = cls._taggers.get(resource_type)
        if not tagger_cls:
            raise ValueError(f"No tagger found for resource type: {resource_type}")
        return tagger_cls()
