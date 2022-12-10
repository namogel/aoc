with open("input") as fd:
    grid = [line.rstrip("\n") for line in fd.readlines()]

WIDTH, HEIGHT = len(grid[0]), len(grid)

# part 1
visible = sum(
    1
    for i in range(WIDTH)
    for j in range(HEIGHT)
    if (
        all(grid[j][i_] < grid[j][i] for i_ in range(i))  # left
        or all(grid[j][i_] < grid[j][i] for i_ in range(i+1, WIDTH))  # right
        or all(grid[j_][i] < grid[j][i] for j_ in range(j))  # top
        or all(grid[j_][i] < grid[j][i] for j_ in range(j+1, HEIGHT))  # bottom
    )
)
print(visible)

# part 2
max_ = max(
    (
        next((k for k, i_ in enumerate(range(i-1, -1, -1), 1) if grid[j][i_] >= grid[j][i]), i) *  # left
        next((k for k, i_ in enumerate(range(i+1, WIDTH), 1) if grid[j][i_] >= grid[j][i]), WIDTH-1-i) *  # right
        next((k for k, j_ in enumerate(range(j-1, -1, -1), 1) if grid[j_][i] >= grid[j][i]), j) *  # top
        next((k for k, j_ in enumerate(range(j+1, HEIGHT), 1) if grid[j_][i] >= grid[j][i]), HEIGHT-1-j)  # bottom
    )
    for i in range(1, WIDTH-1)
    for j in range(1, HEIGHT-1)
)
print(max_)
