import os
import pickle
links = []
filename = 'hot_az_links.pkl'

# Check if the file exists
if os.path.exists(filename):
    # If the file exists, load its contents into a variable
    with open(filename, 'rb') as file:
        prev_links = pickle.load(file)

for link in prev_links:
    if ("/category/" not in link) and ("/author/" not in link):
        links.append(link)
    else:
        print(link)

with open(f'ask_apollo.pkl', 'wb') as file:
        pickle.dump(links,file)
print(len(links))
