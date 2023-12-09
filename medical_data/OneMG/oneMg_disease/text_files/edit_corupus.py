import os
import fileinput

folder_path = './corpus_unedited/'  # Replace with the actual path to your folder
dest_folder_path = './corpus_edited/'
def remove_last_lines(file_path, lines,filename):
    with open(file_path, 'r') as f:
        lines_to_keep = f.readlines()[:-lines]

    dest_file_path = os.path.join(dest_folder_path, filename)

    with open(dest_file_path, 'w') as f:
        f.writelines(lines_to_keep)
        # f.write("========================================================")

for filename in os.listdir(folder_path):
    if filename.endswith('.txt'):  # Only process .txt files
        file_path = os.path.join(folder_path, filename)
        remove_last_lines(file_path,8,filename)
