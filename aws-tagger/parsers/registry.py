from .base import BaseParser


class ParserRegistry:
    """
    A registry class to manage and retrieve parser classes by name.
    This class uses a decorator-based approach to register parser classes.

    Attributes:
        _parsers (dict): A private dictionary to store registered parsers with their names as keys.

    Methods:
        register(name: str) -> Callable:
            A class method that acts as a decorator to register a parser class with a specific name.

        get_parser(name: str) -> Optional[type]:
            A class method to retrieve a registered parser class by its name.
    """

    _parsers = {}

    @classmethod
    def register(cls, name) -> callable:
        """
        Registers a parser class under a given name.

        Args:
            name (str): The name under which the parser class should be registered.

        Returns:
            Callable: A decorator that registers the given class in the registry.

        Example:
            @ParserRegistry.register("json")
            class JSONParser:
                pass
        """

        def wrapper(parser_class):
            cls._parsers[name] = parser_class
            return parser_class

        return wrapper

    @classmethod
    def get_parser(cls, name: str) -> BaseParser:
        """
        Retrieves an instance of a parser class by its registered name.

        Args:
            name (str): The name of the parser class to retrieve.

        Returns:
            BaseParser: An instance of the parser class if found.

        Raises:
            ValueError: If no parser is registered under the given name.

        Example:
            # Assuming a parser named "json" is registered
            json_parser = ParserRegistry.get_parser("json")
            result = json_parser.parse("data.json")
        """
        parser_cls = cls._parsers.get(name)
        if not parser_cls:
            raise ValueError(f"Parser for {name} not found!")
        return parser_cls()

