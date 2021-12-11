with open("input") as fd:
    grid = [list(map(int, line.strip())) for line in fd.readlines()]

width, height = len(grid[0]), len(grid)
for step in range(10000):
    flashed = set()

    for j in range(height):
        for i in range(width):
            grid[j][i] += 1

    while True:
        try:
            j, i = next(
                (j, i)
                for j in range(height)
                for i in range(width)
                if grid[j][i] == 10 and (j, i) not in flashed
            )
        except StopIteration:
            break

        flashed.add((j, i))
        grid[j][i] = 0
        for j_, i_ in (
            (j-1, i-1), (j-1, i), (j-1, i+1),
            (j, i-1), (j, i+1),
            (j+1, i-1), (j+1, i), (j+1, i+1),
        ):
            if 0 <= j_ < height and 0 <= i_ < width and grid[j_][i_] < 10 and (j_, i_) not in flashed:
                grid[j_][i_] += 1

    for (j, i) in flashed:
        grid[j][i] = 0

    if len(flashed) == width * height:
        print(step + 1)
        break
