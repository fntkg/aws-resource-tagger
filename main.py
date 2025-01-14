import csv
import sys
from tagger_factory import AwsResourceTaggerFactory
from utils.csv_utils import find_column_by_suffix

def process_csv(file_path):
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            resource_type_column = find_column_by_suffix(row, "nativeType")
            resource_id_column = find_column_by_suffix(row, "providerUniqueId")
            region_column = find_column_by_suffix(row, "region")

            if not resource_type_column or not resource_id_column or not region_column:
                print("Error: Required columns not found in CSV")
                continue

            resource_type = row[resource_type_column]
            full_resource_id = row[resource_id_column]
            region = row[region_column]
            resource_id = full_resource_id.split('/')[-1]

            # TODO Use your own tag set!
            tags = [
                {"Key": "Environment", "Value": "???"},
                {"Key": "DeploymentType", "Value": "???"},
                {"Key": "Brand", "Value": "???"},
                {"Key": "AppCategory", "Value": "???"}
            ]

            try:
                tagger = AwsResourceTaggerFactory.get_tagger(resource_type, resource_id, tags, region)
                tagger.add_tags()
            except Exception as e:
                print(f"Error processing resource {resource_id}: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py <csv_file_path>")
        sys.exit(1)

    file_path = sys.argv[1]
    process_csv(file_path)
