import re

regex = re.compile(r"x=(-?\d+), y=(-?\d+).*x=(-?\d+), y=(-?\d+)")

with open("input") as fd:
    lines = [tuple(map(int, regex.search(line.rstrip("\n")).groups())) for line in fd.readlines()]


def distance(p1, p2):
    return abs(p2[1] - p1[1]) + abs(p2[0] - p1[0])


def merge(ranges):
    ranges.sort()
    try:
        for i in range(len(ranges)):
            while ranges[i][1] >= ranges[i+1][0]:
                ranges[i][1] = max(ranges[i][1], ranges.pop(i+1)[1])
    except IndexError:
        pass
    return ranges


def part1():
    y = 2000000
    covered, sensors = [], set()
    for xs, ys, xb, yb in lines:
        if ys == y:
            sensors.add(xs)
        if yb == y:
            sensors.add(xb)
        if (d := distance((xs, ys), (xb, yb)) - abs(ys - y)) >= 0:
            covered.append([xs - d, xs + d])

    covered = merge(covered)

    return sum(x2 - x1 + 1 - sum((x1 <= x <= x2) for x in sensors) for x1, x2 in covered)


def part2():
    min_, max_ = 0, 4000000
    for y in range(min_, max_):
        covered = []
        for xs, ys, xb, yb in lines:
            if (d := distance((xs, ys), (xb, yb)) - abs(ys - y)) >= 0:
                covered.append([max(min_, xs - d), min(xs + d, max_)])

        covered = merge(covered)

        if len(covered) > 1:
            (_, x1), (x2, _) = covered
            return (x2 + x1) // 2 * 4000000 + y


print(part1())
print(part2())
