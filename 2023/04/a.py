with open("input") as fd:
    lines = fd.read().splitlines()


def part1():
    s = 0
    for line in lines:
        winning, played = (s.split() for s in line.split(":")[1].split("|"))
        winning = set(winning)
        if (c := sum(c in winning for c in played)) > 0:
            s += 2 ** (c-1)
    return s


def part2():
    deck = {i: 1 for i in range(len(lines))}
    for i, line in enumerate(lines):
        winning, played = (s.split() for s in line.split(":")[1].split("|"))
        winning = set(winning)
        for j in range(i+1, i+1+sum(c in winning for c in played)):
            deck[j] += deck[i]
    return sum(deck.values())
