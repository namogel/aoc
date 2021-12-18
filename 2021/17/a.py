import re

with open("input") as fd:
    m = re.match(r".*x=(-?\d+)\.\.(-?\d+), y=(-?\d+)\.\.(-?\d+)", fd.readlines()[0].strip())

x_min, x_max, y_min, y_max = map(int, m.groups())


def fire(vx, vy):
    x, y = 0, 0
    while True:
        x += vx
        y += vy
        if vx > 0:
            vx -= 1
        elif vx < 0:
            vx += 1
        vy -= 1
        if x_min <= x <= x_max and y_min <= y <= y_max:
            return True
        if x > x_max or y < y_min:
            return False


def solve():
    a = set()
    for vx in range(1, 1000):
        for vy in range(-1000, 1000):
            if fire(vx, vy):
                a.add((vx, vy))
    return len(a)


print(solve())
