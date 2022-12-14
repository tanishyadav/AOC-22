with open("data.txt", "rt") as file:
    data = file.read().split('\n\n')

monkeys = [[] for _ in range(len(data))]

for _ in range()
for i, monkey in enumerate(monkeys):
    d = data[i].split('\n')
    items = [int(x) for x in d[1].strip()[16:].split(', ')]
    op = d[2].split(' ')[-2:]
    op[1] = int(op[1])
    t