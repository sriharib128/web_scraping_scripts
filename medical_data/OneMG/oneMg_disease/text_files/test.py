import pickle
  
# Open the file in binary mode
with open('disease.pkl', 'rb') as file:
    # Call load method to deserialze
    disease_links = pickle.load(file)

with open('letter.pkl', 'rb') as file:
    # Call load method to deserialze
    letter_links = pickle.load(file)


sum=0

for a in range(len(letter_links)):
    print (f"==> {a}")
    sum+=len(disease_links[a])
    for b in range(len(disease_links[a])):
        # get_text(disease_links[a][b],a,b)
        print(f" {b} - {disease_links[a][b]}")
    print("---------------------------")
print(f'sum = {sum}')