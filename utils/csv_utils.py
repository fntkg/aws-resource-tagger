def find_column_by_suffix(row, suffix):
    return next((col for col in row if col.endswith(suffix)), None)