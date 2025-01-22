import csv
import sys
from tagger_factory import AwsResourceTaggerFactory
from utils.csv_utils import find_column_by_suffix

def process_csv(file_path):
    """
    Processes a CSV file to extract AWS resource information and apply tags to them.

    Args:
        file_path (str): The path to the CSV file to be processed.

    The function reads the CSV file, extracts relevant columns for AWS resource tagging,
    and attempts to tag each resource with predefined tags.
    """
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Identify required columns using suffix search
            resource_type_column = find_column_by_suffix(row, "nativeType")
            resource_id_column = find_column_by_suffix(row, "providerUniqueId")
            region_column = find_column_by_suffix(row, "region")
            account_id_column = find_column_by_suffix(row, "subscriptionExternalId")

            # Validate presence of essential columns
            if not resource_type_column or not resource_id_column or not region_column:
                print("Error: Required columns not found in CSV")
                continue

            # Extract necessary values
            resource_type = row[resource_type_column]
            full_resource_id = row[resource_id_column]
            region = row[region_column]
            account_id = row.get(account_id_column, "")  # Handle missing account_id gracefully
            resource_id = full_resource_id.split('/')[-1]  # Extract unique resource identifier

            # Predefined tags to be applied to resources
            tags = [
                {"Key": "DataClassification", "Value": "Confidential"}
            ]
            # {"Key": "AdminEmail", "Value": ""} 

            try:
                # Obtain a tagger instance from the factory and apply tags
                tagger = AwsResourceTaggerFactory.get_tagger(resource_type, resource_id, tags, region, account_id, full_resource_id)
                tagger.add_tags()
            except Exception as e:
                print(f"Error processing resource {resource_id}: {e}")

if __name__ == "__main__":
    """
    Entry point of the script. Expects a CSV file path as a command-line argument.
    """
    if len(sys.argv) != 2:
        print("Usage: python main.py <csv_file_path>")
        sys.exit(1)

    file_path = sys.argv[1]
    process_csv(file_path)
