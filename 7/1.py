"""
filesystem(dict):
    files(dict):
        file_name: size
    dirs(dict):
        dir_name: files(dict)
"""



with open("data.txt", "rt") as file:
    data = file.read().split('$')


pwd = []

dirs = {}

def handle_ls(d):
    global dirs
    p = '/'.join(pwd)
    dirs[p] = 0
    for entry in d:
        if not entry:
            continue
        print(entry)
        entry = entry.split(' ')
        if entry[0] == 'dir':
            continue
        dirs[p] += int(entry[0])


print(data)
for command in data[2:]: #skip $ cd /
    print(command)
    com = [x.strip() for x in command.split('\n')]
    print(com)
    c = com[0].split(' ')
    if c[0] == 'cd':
        if c[1] == '..':
            pwd = pwd[:-1]
        else:
            pwd.append(c[1])
    elif c[0] != 'ls':
        print('WTF!')
        print(c)
    handle_ls(com[1:])

print(dirs)