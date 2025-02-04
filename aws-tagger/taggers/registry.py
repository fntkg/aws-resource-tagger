from .base import AwsResourceTagger


class TaggerRegistry:
    """
    A registry for managing AWS resource taggers.

    This class allows dynamic registration and retrieval of taggers responsible for
    tagging different types of AWS resources. It follows the **Registry Pattern**
    to ensure that taggers can be registered and retrieved efficiently.

    Attributes:
        _taggers (dict): A dictionary mapping resource types (str) to their respective tagger classes.
        _instances (dict): A dictionary to cache singleton instances for each tagger, keyed by resource type and region.
    """

    _taggers = {}
    _instances = {}  # Dictionary for caching tagger instances

    @classmethod
    def register(cls, name: str) -> callable:
        """
        A decorator to register a tagger class under a specified resource type.
        """

        def wrapper(tagger_class):
            cls._taggers[name] = tagger_class
            return tagger_class

        return wrapper

    @classmethod
    def get_tagger(cls, resource_type: str, region: str) -> AwsResourceTagger:
        """
        Retrieves the tagger instance for a given AWS resource type and region.

        Args:
            resource_type (str): The type of AWS resource (e.g., "ec2", "s3").
            region (str): The AWS region for which the tagger should be used.

        Returns:
            AwsResourceTagger: An instance of the registered tagger class, unique per resource type and region.

        Raises:
            ValueError: If no tagger is registered for the given resource type.
        """
        # Build a key combining resource type and region
        key = f"{resource_type}-{region}"

        # Check if an instance for this resource type and region already exists
        if key in cls._instances:
            return cls._instances[key]

        # Retrieve the corresponding tagger class
        tagger_cls = cls._taggers.get(resource_type)
        if not tagger_cls:
            raise ValueError(f"No tagger found for resource type: {resource_type}")

        # Create a new instance passing the region and cache it
        instance = tagger_cls(region)
        cls._instances[key] = instance
        return instance
