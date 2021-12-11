with open("input") as fd:
    for line in fd:
        positions = sorted(map(int, line.strip().split(",")))


def nsum(n):
    return int((n * (n + 1)) / 2)


def fuel(p1):
    return sum(nsum(abs(p1 - p2)) for p2 in positions)


print(min(map(fuel, range(positions[0], positions[-1] + 1))))

# 93397632
