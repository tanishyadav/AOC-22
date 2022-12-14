with open("data.txt", "rt") as file:
    data = file.read().splitlines()

s = 0
for line in data:
    pair = line.split(',')
    pair = [[int(y) for y in x.split('-')] for x in pair]
    if pair[0][0] <= pair[1][0] and pair[0][1] >= pair[1][1]:
        s += 1
    elif pair[1][0] <= pair[0][0] and pair[1][1] >= pair[0][1]:
        s += 1

print(s)