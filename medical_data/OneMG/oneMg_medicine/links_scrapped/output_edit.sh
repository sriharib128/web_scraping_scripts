#!/bin/bash

input_file="corpus_2.txt"

# Remove lines with less than three words
filtered_content=$(awk 'NF >= 3' "$input_file")

# Replace ". " with ".\n"
modified_content=$(echo "$filtered_content" | sed 's/\(\.\) /\1\n/g')

# Save the modified content back to the input file
echo "$modified_content" > "$input_file"

echo "Lines with less than three words removed and replacements made in $input_file."
