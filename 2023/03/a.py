grid: list[str] = []
with open("input") as fd:
    for line_ in fd.readlines():
        grid.append(line_.rstrip("\n"))


height = len(grid)
width = len(grid[0])


def is_symbol(c: str):
    return not c.isdigit() and c != "."


def is_part(i, j1, j2):
    left = (j1 > 0 and is_symbol(grid[i][j1-1]))
    right = (j2 < width-1 and is_symbol(grid[i][j2+1]))
    up = (i > 0 and any(is_symbol(grid[i-1][j_]) for j_ in range(max(0, j1-1), min(width, j2+2))))
    down = (i < height-1 and any(is_symbol(grid[i+1][j_]) for j_ in range(max(0, j1-1), min(width, j2+2))))
    return left or right or up or down


def handle_line(i, line, start):
    s = 0
    try:
        j1 = next(j for j in range(start, width) if line[j].isdigit())
    except StopIteration:
        return s
    j2 = next((j for j in range(j1 + 1, width) if not line[j].isdigit()), width)

    if is_part(i, j1, j2):
        s += int(line[j1:j2])

    return s + handle_line(i, line, j2 + 1)


def part1():
    return sum(handle_line(i, line, 0) for i, line in enumerate(grid))


def get_digit_xs(line, j):
    return (
        next((j_+1 for j_ in range(j, -1, -1) if not line[j_].isdigit()), 0),
        next((j_-1 for j_ in range(j, width) if not line[j_].isdigit()), width-1)
    )


def get_around(i, j):
    around = []
    if grid[i][j].isdigit():
        around.append((i, *get_digit_xs(grid[i], j)))
    else:
        if j > 0 and grid[i][j-1].isdigit():
            around.append((i, *get_digit_xs(grid[i], j-1)))
        if j < width-1 and grid[i][j+1].isdigit():
            around.append((i, *get_digit_xs(grid[i], j+1)))
    return around


def part2():
    s = 0
    for i, line in enumerate(grid):
        for j in range(width):
            if line[j] != "*":
                continue
            around = get_around(i, j)
            if i > 0:
                around.extend(get_around(i-1, j))
            if i < height - 1:
                around.extend(get_around(i+1, j))
            if len(around) == 2 and all(is_part(*d) for d in around):
                q = 1
                for i_, j1, j2 in around:
                    q *= int(grid[i_][j1:j2+1])
                s += q
    return s
