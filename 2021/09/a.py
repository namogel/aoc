from functools import reduce

with open("input") as fd:
    grid = [l.strip() for l in fd.readlines()]

width = len(grid[0])
height = len(grid)
basins = {}
for j in range(height):
    for i in range(width):
        cell = grid[j][i]
        if (
            (i == 0 or cell < grid[j][i-1]) and
            (i == width - 1 or cell < grid[j][i+1]) and
            (j == 0 or cell < grid[j-1][i]) and
            (j == height - 1 or cell < grid[j+1][i])
        ):
            basins[(j, i)] = {(j, i)}

for p, basin in basins.items():
    visited = set()
    j, i = p
    while True:
        for j_, i_ in (
            (j, i + 1), (j, i - 1),
            (j + 1, i), (j - 1, i),
        ):
            if (
                (j_, i_) not in basin and
                (0 <= j_ < height) and
                (0 <= i_ < width) and
                (grid[j][i] < grid[j_][i_] < "9")
            ):
                basin.add((j_, i_))
        visited.add((j, i))
        try:
            j, i = next(iter(basin - visited))
        except StopIteration:
            break

biggest_basins = sorted(map(len, basins.values()), reverse=True)
print(reduce(lambda x, y: x * y, biggest_basins[:3]))
