with open("all.txt", "r") as fi:
    links = fi.readlines()

for a in range(10):
    i = a
    links_10 = []
    while i < len(links):
        links_10.append(links[i])
        i = i + 10

    with open(f"links_10_{a}.txt", "w") as file:
        string = "".join(links_10)
        file.write(string)

    print(f"Number of lines in links_10_{a}.txt: {len(links_10)}")
