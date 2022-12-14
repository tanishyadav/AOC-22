with open("data.txt", "rt") as file:
    data = file.read().split('$')

def handle_ls(d):
    global dirs
    for entry in d:
        if not entry:
            continue
        entry = entry.split(' ')
        if entry[0] == 'dir':
            continue
        for i in range(len(pwd)):
            p = '/'.join(pwd[:i+1])
            if p in dirs.keys():
                dirs[p] += int(entry[0])
            else:
                dirs[p] = int(entry[0])

pwd = ['/']
dirs = {}

for command in data[2:]: #skip $ cd /
    com = [x.strip() for x in command.split('\n')]
    c = com[0].split(' ')
    if c[0] == 'cd':
        if c[1] == '..':
            pwd = pwd[:-1]
        else:
            pwd.append(c[1])
        continue
    handle_ls(com[1:])

s = 30000000 - (70000000 - dirs['/'])
for size in sorted(dirs.values()):
    if size >= s:
        print(size)
        break