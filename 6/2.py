with open("data.txt", "rt") as file:
    data = file.read()

for i in range(3, len(data)):
    if len({data[i-k] for k in range(14)}) == 14:
        print(i+1)
        break