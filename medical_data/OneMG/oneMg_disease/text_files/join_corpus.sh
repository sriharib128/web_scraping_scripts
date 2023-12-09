#!/bin/bash

folder_path="./corpus_edited"  # Replace with the actual path to your folder
output_file="corpus.txt"     # Specify the name of the output file

cat "$folder_path"/*.txt > "$output_file"
