from abc import ABC, abstractmethod

class BaseParser(ABC):
    """
    Abstract base class for implementing a parsing strategy in the Strategy Pattern.

    This class defines the interface that all concrete parsers must implement. It ensures
    that any subclass provides a `parse` method, which is responsible for processing
    a given input file and extracting relevant data.

    The purpose of this interface is to support multiple file formats (e.g., CSV, JSON,
    plain text) by allowing different parser implementations to handle various input structures
    while maintaining a consistent API.
    """

    @staticmethod
    @abstractmethod
    def parse(file_path: str) -> list:
        """
        Abstract method for parsing a given file and extracting data.

        This method must be implemented by subclasses to define the specific logic for
        reading and processing a file. The extracted data should be returned in a standardized
        format (A list of AWS resource ARNs).

        Args:
            file_path (str): The path to the file that needs to be parsed.

        Returns:
            list: A list of AWS Resource ARNs extracted from the input file.
        Raises:
            NotImplementedError: If the method is not implemented in a subclass.
        """
        pass
