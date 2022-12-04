part1 = part2 = 0

with open("input") as fd:
    for line in fd.readlines():
        p1, p2 = (tuple(map(int, p.split("-"))) for p in line.rstrip("\n").split(","))
        if p1[0] <= p2[0] <= p2[1] <= p1[1] or p2[0] <= p1[0] <= p1[1] <= p2[1]:
            part1 += 1
        if p1[0] <= p2[0] <= p1[1] or p2[0] <= p1[0] <= p2[1]:
            part2 += 1

print(part1)
print(part2)
