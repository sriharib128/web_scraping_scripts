#!/bin/bash

input_file="corpus.txt"   # Replace with the path to your input file
lines_per_file=10000
output_prefix="output_"

split -l $lines_per_file $input_file $output_prefix

# Rename the output files to have .txt extension
for file in ${output_prefix}??; do
    mv "$file" "${file}.txt"
done

# Convert each text file to DOCX using pandoc
for txt_file in ${output_prefix}*.txt; do
    docx_file="${txt_file%.txt}.docx"
    pandoc "$txt_file" -o "$docx_file"
done