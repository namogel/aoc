with open("input") as fd:
    grid = [line.rstrip("\n") for line in fd.readlines()]

WIDTH, HEIGHT = len(grid[0]), len(grid)

# part 1
visited = set()
for j, line in enumerate(grid):
    highest = "-1"
    for i, h in enumerate(line):
        if h > highest:
            highest = h
            visited.add((i, j))
    highest = "-1"
    for i, h in enumerate(line[::-1]):
        if h > highest:
            highest = h
            visited.add((WIDTH-1-i, j))
for i in range(WIDTH):
    column = "".join(grid[j][i] for j in range(HEIGHT))
    highest = "-1"
    for j, h in enumerate(column):
        if h > highest:
            highest = h
            visited.add((i, j))
    highest = "-1"
    for j, h in enumerate(column[::-1]):
        if h > highest:
            highest = h
            visited.add((i, HEIGHT-1-j))
print(len(visited))

# part 2
max_ = max(
    (
        next((k for k, i_ in enumerate(range(i-1, -1, -1), 1) if grid[j][i_] >= grid[j][i]), i) *
        next((k for k, i_ in enumerate(range(i+1, WIDTH), 1) if grid[j][i_] >= grid[j][i]), WIDTH-1-i) *
        next((k for k, j_ in enumerate(range(j-1, -1, -1), 1) if grid[j_][i] >= grid[j][i]), j) *
        next((k for k, j_ in enumerate(range(j+1, HEIGHT), 1) if grid[j_][i] >= grid[j][i]), HEIGHT-1-j)
    )
    for i in range(1, WIDTH-1)
    for j in range(1, HEIGHT-1)
)
print(max_)
