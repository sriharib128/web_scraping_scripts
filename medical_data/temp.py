import pickle
import re 

pickle_file = ["./AskApollo/ask_apollo_links.pkl","./max/max_procedures_links.pkl","./medyblog/medyblog_links.pkl","./OneMG/oneMg_disease/only_link.txt"]

with open(pickle_file[-1], 'r') as file:
    # prev_links = pickle.load(file)
    prev_links = file.readlines()

for temp in prev_links:
    words = temp.split("/")
    temp_word = words[-1].replace("-", " ").split(" ")
    print(" ".join(temp_word[:-1]))