import string

with open("data.txt", "rt") as file:
    data = file.read().splitlines()

priority = dict()
priority.update({c: i for i, c in enumerate(string.ascii_lowercase, start=1)})
priority.update({c: i for i, c in enumerate(string.ascii_uppercase, start=27)})

l = 0
s = 0
while l < len(data):
    s += priority[(set(data[l]) & set(data[l+1]) & set(data[l+2])).pop()]
    l += 3

print(s)