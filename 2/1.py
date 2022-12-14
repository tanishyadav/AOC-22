with open("data.txt", "rt") as file:
    data = file.read().splitlines()

opponent = {'A': 'ROCK', 'B': 'PAPER', 'C': 'SCISSOR'}
you = {'X': 'ROCK', 'Y': 'PAPER', 'Z': 'SCISSOR'}

shape_score = {'X': 1, 'Y': 2, 'Z': 3}

def get_outcome(game):
    game = [opponent[game[0]], you[game[1]]]
    if game[0] == game[1]:
        return 3
    elif game in [['ROCK', 'PAPER'], ['PAPER', 'SCISSOR'], ['SCISSOR', 'ROCK']]:
        return 6
    elif game in [['ROCK', 'SCISSOR'], ['PAPER', 'ROCK'], ['SCISSOR', 'PAPER']]:
        return 0

score = 0
for line in data:
    game = line.split(' ')
    score += shape_score[game[1]] + get_outcome(game)

print(score)