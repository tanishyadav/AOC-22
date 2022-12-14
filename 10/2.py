with open("data.txt", "rt") as file:
    data = file.read().split('\n')

def printc(*args):
    print(*args, end='', flush=True)

X = 1
cycle = 1
aip = False # add in progress

i = 0
while i < len(data):
    if ((x := cycle % 40) or (x := 40)) and x in range(X, X+3):
        printc('#')
    else:
        printc('.')
    if not cycle % 40:
        printc('\n')
    cycle += 1
    if aip:
        aip = False
        X += add
        continue
    if data[i] != "noop":
        add = int(data[i].split(' ')[1])
        aip = True
    i += 1