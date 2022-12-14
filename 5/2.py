def parse_stacks(raw):
    N = int(raw[-1].strip().split(' ')[-1])
    stacks = [[] for _ in range(N)]
    for line in raw[::-1][1:]:
        line = list(line)
        for n in range(N):
            line.pop(0)
            if (x := line.pop(0)) != ' ':
                stacks[n].append(x)
            line.pop(0)
            if n < N - 1:
                line.pop(0)
    return stacks


with open("data.txt", "rt") as file:
    data = file.read()
raw_stacks, instructions = data.split('\n\n')
stacks = parse_stacks(raw_stacks.split('\n'))

for line in instructions.split('\n'):
    line = line.split(' ')
    n, src, dest = int(line[1]), int(line[3]) - 1, int(line[5]) - 1
    stacks[dest].extend(stacks[src][-n:])
    del stacks[src][-n:]

print(''.join(stack[-1] for stack in stacks))
