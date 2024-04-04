import csv

input_file_path = 'data/listings.csv'
output_file_path = 'data/listings_clean.csv'

# Columns to keep
columns_to_keep = [
    'id', 'name', 'host_id', 'host_name', 'host_is_superhost',
    'neighbourhood', 'neighbourhood_group_cleansed', 'price',
    'beds', 'review_scores_rating'
]

# Open the input file for reading and the output file for writing
with open(input_file_path, mode='r', encoding='utf-8') as infile, \
     open(output_file_path, mode='w', encoding='utf-8', newline='') as outfile:

    reader = csv.DictReader(infile)
    writer = csv.DictWriter(outfile, fieldnames=columns_to_keep)
    writer.writeheader()
    
    for row in reader:
        # Check if 'review_scores_rating' is missing
        if not row['review_scores_rating'].strip():
            continue  # Skip this row
        
        # Extract only the desired columns
        filtered_row = {col: row[col] for col in columns_to_keep if col in row}
        writer.writerow(filtered_row)