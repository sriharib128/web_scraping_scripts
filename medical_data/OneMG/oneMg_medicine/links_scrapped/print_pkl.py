import pickle

for a in range(26):
    with open(f"medicine_links_{a}.pkl","rb") as fi:
        links = pickle.load(fi)
    links.sort()
    with open(f"./medicine_links_text/medicine_links_{a}.txt","w") as fi:
        for link in links:
            print(link,file = fi)