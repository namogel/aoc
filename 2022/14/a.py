rocks, sands = set(), set()

with open("input") as fd:
    for line in fd.readlines():
        intersections = [tuple(map(int, i.split(","))) for i in line.rstrip("\n").split(" -> ")]
        for i in range(len(intersections) - 1):
            (x1, y1), (x2, y2) = sorted(intersections[i:i+2])
            rocks.update({(x, y) for x in range(x1, x2+1) for y in range(y1, y2+1)})


MAX_Y = max(r[1] for r in rocks)
MIN_X = min(r[0] for r in rocks)
MAX_X = max(r[0] for r in rocks)


def draw():
    for y in range(MAX_Y+3):
        for x in range(MIN_X-10, MAX_X+10):
            if (x, y) in rocks:
                print("#", end="")
            elif (x, y) in sands:
                print("o", end="")
            else:
                print(".", end="")
        print()
    print()


def part1():
    while True:
        s = (500, 0)
        while True:
            if s[1] > MAX_Y:
                return len(sands)
            try:
                s = next(
                    s_ for s_ in ((s[0], s[1]+1), (s[0]-1, s[1]+1), (s[0]+1, s[1]+1))
                    if s_ not in rocks and s_ not in sands
                )
            except StopIteration:
                sands.add(s)
                break


def part2():
    while True:
        s = (500, 0)
        while True:
            try:
                s = next(
                    s_ for s_ in ((s[0], s[1]+1), (s[0]-1, s[1]+1), (s[0]+1, s[1]+1))
                    if s_ not in rocks and s_ not in sands and s[1] <= MAX_Y
                )
            except StopIteration:
                sands.add(s)
                if s == (500, 0):
                    return len(sands)
                break


print(part1())
print(part2())
