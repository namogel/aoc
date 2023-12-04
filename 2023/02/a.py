MAX_COLORS = {"red": 12, "green": 13, "blue": 14}


def is_ok(line):
    for hand in line.rstrip("\n").split(":")[1].split(";"):
        for data in hand.split(","):
            count, color = data.strip().split(" ")
            if int(count) > MAX_COLORS[color]:
                return False
    return True


def part1():
    with open("input") as fd:
        return sum(i for i, line in enumerate(fd.readlines(), 1) if is_ok(line))


def power(line):
    maxs = {"red": 0, "green": 0, "blue": 0}
    for hand in line.rstrip("\n").split(":")[1].split(";"):
        for data in hand.split(","):
            count, color = data.strip().split(" ")
            maxs[color] = max(int(count), maxs[color])
    return maxs["red"] * maxs["green"] * maxs["blue"]


def part2():
    with open("input") as fd:
        return sum(map(power, fd.readlines()))
