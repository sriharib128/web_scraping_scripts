#!/bin/bash

source_folder="./corpus_unedited/"
destination_folder="./corpus_edited/"
rm -rf "$destination_folder"
lines_to_remove=8
new_line="\n\n===============================================\n\n"

mkdir -p "$destination_folder"

for file in "$source_folder"/*.txt; do
    filename=$(basename "$file")
    output_file="$destination_folder/$filename"
    head -n -$lines_to_remove "$file" > "$output_file"
    echo -e "$new_line" >> "$output_file"
done

echo "Operation completed."
