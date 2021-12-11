with open("input") as fd:
    winds = [
        tuple(tuple(map(int, p.split(","))) for p in line.split(" -> "))
        for line in fd.readlines()
    ]

effects = [[0 for _ in range(1000)] for _ in range(1000)]
for (x1, y1), (x2, y2) in winds:
    wy = 1 if y2 >= y1 else -1
    wx = 1 if x2 >= x1 else -1
    if x1 == x2:
        for y in range(y1, y2 + wy, wy):
            effects[y][x1] += 1
    elif y1 == y2:
        for x in range(x1, x2 + wx, wx):
            effects[y1][x] += 1
    else:
        for y, x in zip(range(y1, y2 + wy, wy), range(x1, x2 + wx, wx)):
            effects[y][x] += 1

print(sum(e >= 2 for row in effects for e in row))
