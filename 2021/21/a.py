from collections import Counter


def make_dice():
    while True:
        yield from range(1, 101)


class Player:
    def __init__(self, position):
        self.position = position
        self.score = 0


def part1():
    players = {0: Player(P1), 1: Player(P2)}
    d = make_dice()
    i = 0
    while all(p.score < 1000 for p in players.values()):
        p = players[i % 2]
        i += 1
        p.position += (sum(next(d) for _ in range(3))) % 10
        if p.position > 10:
            p.position %= 10
        p.score += p.position

    print(i * 3 * players[i % 2].score)


def make_rolls():
    def roll(v, n):
        if n == 3:
            rolls_[v] += 1
        else:
            for r in (1, 2, 3):
                roll(v + r, n + 1)

    rolls_ = Counter()
    roll(0, 0)
    return rolls_


def part2():
    wins = [0, 0]
    plays = {(P1, 0, P2, 0): 1}
    rolls = make_rolls()
    while plays:
        round_plays = list(plays.items())
        plays = Counter()
        for (p1, s1, p2, s2), games in round_plays:
            for r1, c1 in rolls.items():
                new_p1 = (p1 - 1 + r1) % 10 + 1
                new_s1 = s1 + new_p1
                if new_s1 >= 21:
                    wins[0] += games * c1
                else:
                    for r2, c2 in rolls.items():
                        new_p2 = (p2 - 1 + r2) % 10 + 1
                        new_s2 = s2 + new_p2
                        if new_s2 >= 21:
                            wins[1] += games * c1 * c2
                        else:
                            plays[(new_p1, new_s1, new_p2, new_s2)] += games * c1 * c2

    print(max(wins))


# P1, P2 = 4, 8
P1, P2 = 6, 8
# part1()
part2()

