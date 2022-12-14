with open("data.txt", "rt") as file:
    data = file.read().splitlines()

cal = 0
max_cal = cal

for line in data:
    if line:
        cal += int(line)
    else:
        max_cal = max(max_cal, cal)
        cal = 0

print(max_cal)