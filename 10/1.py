with open("data.txt", "rt") as file:
    data = file.read().split('\n')

critical = [20, 60, 100, 140, 180, 220]

X = 1
cycle = 1
aip = False # add in progress

score = 0
i = 0
while i < len(data):
    if cycle in critical:
        score += X*cycle
    cycle += 1
    if aip:
        aip = False
        X += add
        continue
    if data[i] != "noop":
        add = int(data[i].split(' ')[1])
        aip = True
    i += 1

print(score)