# #!/bin/bash


# # In Bash, ${variable%substring} removes the shortest match of substring from the end of the value of variable. In your script, docx_file is the variable representing the path to the input .docx file.

# # Loop through .docx files ending with "telugu.docx"
# for docx_file in ./*telugu.docx; do
#     if [ -f "$docx_file" ]; then
#         txt_file="${docx_file%.docx}.txt"
#         pandoc -s "$docx_file" -t plain -o "$txt_file"
#         echo "Converted $docx_file to $txt_file"
#     fi
# done

# #!/bin/bash

# folder_path="."  # Replace with the actual path to your folder
output_file="corpus_telugu.txt"     # Specify the name of the output file

# cat "$folder_path"/*telugu.txt > "$output_file"

docx_file="${txt_file%.txt}.docx"

pandoc "$output_file" -o "$docx_file"