def find_column_by_suffix(row, suffix):
    return next((col for col in row if col.endswith(suffix)), None)

def get_s3_bucket_name(resource_id):
    return resource_id.split(':')[-1]