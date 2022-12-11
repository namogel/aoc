x, ops, s = 1, [], 0
with open("input") as fd:
    for line in fd.readlines():
        line = line.rstrip("\n")
        ops.append(0)
        if line != "noop":
            ops.append(int(line.split()[1]))

# part1
for i, v in enumerate(ops, 1):
    if i == 20 or not ((i + 20) % 40):
        s += x * i
    x += v
print(s)

# part2
for i, v in enumerate(ops):
    print("#" if i % 40 in (x - 1, x, x + 1) else ".", end="")
    x += v
    if not (i+1) % 40:
        print()
