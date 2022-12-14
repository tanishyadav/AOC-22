with open("data.txt", "rt") as file:
    data = file.read().splitlines()

opponent = {'A': 'ROCK', 'B': 'PAPER', 'C': 'SCISSOR'}
you = {'X': 'LOSE', 'Y': 'DRAW', 'Z': 'WIN'}
you_score = {'X': 0, 'Y': 3, 'Z': 6}
shape_score = {'ROCK': 1, 'PAPER': 2, 'SCISSOR': 3}
win = {'ROCK': 'PAPER', 'PAPER': 'SCISSOR', 'SCISSOR': 'ROCK'}
lose = {y: x for x, y in win.items()}

def get_shape(opponent, outcome):
    if outcome == 'DRAW':
        return opponent
    elif outcome == 'WIN':
        return win[opponent]
    elif outcome == 'LOSE':
        return lose[opponent]

score = 0
for line in data:
    game = line.split(' ')
    score += shape_score[get_shape(opponent[game[0]], you[game[1]])] + you_score[game[1]]

print(score)