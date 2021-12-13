from operator import itemgetter

dots, folds = [], []
with open("input") as fd:
    for line in fd:
        line = line.strip()
        if line:
            if line.startswith("fold"):
                folds.append(line[11:].split("="))
                folds[-1][1] = int(folds[-1][1])
            else:
                dots.append(list(map(int, line.split(","))))


for d, c in folds:
    for i, (x, y) in enumerate(dots):
        if d == "x" and x > c:
            dots[i][0] = 2 * c - x
        if d == "y" and y > c:
            dots[i][1] = 2 * c - y


dots = set(map(tuple, dots))
width, height = (max(dots, key=itemgetter(i))[i] for i in (0, 1))
print("\n".join("".join("*" if (x, y) in dots else " " for x in range(width + 1)) for y in range(height + 1)))
