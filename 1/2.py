with open("data.txt", "rt") as file:
    data = file.read().split('\n\n')

calories = list()

for elf in data:
    calories.append(sum(int(cal) for cal in elf.split('\n')))

print(sum(sorted(calories)[-3:]))