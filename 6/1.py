with open("data.txt", "rt") as file:
    data = file.read()

for i in range(3, len(data)):
    if len({data[i-3], data[i-2], data[i-1], data[i]}) == 4:
        print(i+1)
        break