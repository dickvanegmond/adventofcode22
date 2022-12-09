with open('day2/input.txt') as f:
    lines = f.read().splitlines() 

moves = []
for line in lines:
    moves.append(tuple(line.split(' ')))

scoresOwnMove = {
    "X" : 1,
    "Y" : 2,
    "Z" : 3
}

scoresMatchOutcome = {
    "A" : {"X": 3, "Y": 6, "Z": 0},
    "B" : {"X": 0, "Y": 3, "Z": 6},
    "C" : {"X": 6, "Y": 0, "Z": 3}
}


def scoreOwnMove(move):
    return(scoresOwnMove[move[1]])

def scoreMatch(move):
    return(scoresMatchOutcome[move[0]][move[1]])




totalScore = 0
for move in moves:
    totalScore += scoreOwnMove(move) + scoreMatch(move)

# Answer part 1
print(totalScore)

outcome = {
    "X" : 0,
    "Y" : 3,
    "Z" : 6
}

ownMoveBasedOnOutcome = {
    "A" : {3: 1, 6: 2, 0: 3},
    "B" : {0: 1, 3: 2, 6: 3},
    "C" : {6: 1, 0: 2, 3: 3}
}


def moveBasedOnOutcome(move):
    firstHalf = outcome[move[1]]
    secondHalf = ownMoveBasedOnOutcome[move[0]][firstHalf]
    return firstHalf + secondHalf


totalScorePart2 = 0
for move in moves:
    totalScorePart2 += moveBasedOnOutcome(move)

# Anwer part 2
print(totalScorePart2)