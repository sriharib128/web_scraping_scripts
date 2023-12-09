# Create the "sorted" subdirectory if it doesn't exist
mkdir -p ./sorted

# Loop through each .txt file in the current directory
for file in *.txt; do
  # Sort the file and save the result in the "sorted" subdirectory
  sort "$file" -u > "./sorted/$file"
done
