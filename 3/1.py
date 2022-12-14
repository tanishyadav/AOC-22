import string

with open("data.txt", "rt") as file:
    data = file.read().splitlines()

priority = dict()
priority.update({c: i for i, c in enumerate(string.ascii_lowercase, start=1)})
priority.update({c: i for i, c in enumerate(string.ascii_uppercase, start=27)})

s = 0
for line in data:
    c1 = set(line[:len(line)//2])
    c2 = set(line[len(line)//2:])
    s += priority[(c1 & c2).pop()]

print(s)