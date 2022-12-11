xh, yh = 0, 0
visited = set()
# LENGTH = 1  # part 1
LENGTH = 9  # part 2

knots = [[0, 0] for _ in range(LENGTH)]
with open("input") as fd:
    for line in fd.readlines():
        direction, count = line.rstrip("\n").split()
        for _ in range(int(count)):
            xh += {"L": -1, "R": 1}.get(direction, 0)
            yh += {"U": -1, "D": 1}.get(direction, 0)
            for i in range(LENGTH):
                x2, y2 = knots[i]
                x1, y1 = (xh, yh) if i == 0 else knots[i-1]
                if (y2 - y1)**2 > 1 or (x2 - x1)**2 > 1:
                    knots[i][0] += (1 if x1 > x2 else -1) * (x1 != x2)
                    knots[i][1] += 1 if y1 > y2 else -1 * (y2 != y1)
            visited.add(tuple(knots[-1]))

print(len(visited))
