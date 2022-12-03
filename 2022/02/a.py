# A for Rock, B for Paper, and C for Scissors
# X for Rock, Y for Paper, and Z for Scissors
# Rock defeats Scissors, Scissors defeats Paper, and Paper defeats Rock
# 1 for Rock, 2 for Paper, and 3 for Scissors
# 0 if you lost, 3 if the round was a draw, and 6 if you won
# X: win, Y: draw, Z: lose

WIN = 6
DRAW = 3
LOSE = 0
ROCK = 1
PAPER = 2
SCISSOR = 3

POINTS_P1 = {
    "X": {  # rock
        "A": DRAW + ROCK,
        "B": LOSE + ROCK,
        "C": WIN + ROCK,
    },
    "Y": {  # paper
        "A": WIN + PAPER,
        "B": DRAW + PAPER,
        "C": LOSE + PAPER,
    },
    "Z": {  # scissor
        "A": LOSE + SCISSOR,
        "B": WIN + SCISSOR,
        "C": DRAW + SCISSOR,
    }
}

POINTS_P2 = {
    "X": {
        "A": LOSE + SCISSOR,  # rock
        "B": LOSE + ROCK,  # paper
        "C": LOSE + PAPER,  # scissor
    },
    "Y": {  # paper
        "A": DRAW + ROCK,  # rock
        "B": DRAW + PAPER,  # paper
        "C": DRAW + SCISSOR,  # scissor
    },
    "Z": {  # scissor
        "A": WIN + PAPER,  # rock
        "B": WIN + SCISSOR,  # paper
        "C": WIN + ROCK,  # scissor
    }
}

part1 = part2 = 0
with open("input") as fd:
    for line in fd.readlines():
        him, me = line.rstrip("\n").split(" ")
        part1 += POINTS_P1[me][him]
        part2 += POINTS_P2[me][him]

print(part1)
print(part2)
