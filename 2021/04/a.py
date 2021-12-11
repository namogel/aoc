from itertools import chain


def chunk(grids):
    return (grids[i:i+6][1:] for i in range(0, len(grids), 6))


def split_line(l):
    return [int(l[i:i+3].strip()) for i in range(0, 14, 3)]


with open("input") as fd:
    picked, *grids = fd.read().splitlines()
    grids = [[split_line(l) for l in lines] for lines in chunk(grids)]

scores = []
for n in map(int, picked.split(",")):
    for grid in list(grids):
        for row in grid:
            for i in range(5):
                if row[i] == n:
                    row[i] = -1
        if any(sum(row) == -5 for row in chain(grid, zip(*grid))):
            scores.append(sum(v for row in grid for v in row if v != -1) * n)
            grids.remove(grid)

print(scores[0])
print(scores[-1])
