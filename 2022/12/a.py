from string import ascii_letters

with open("input") as fd:
    grid = [line.rstrip("\n") for line in fd.readlines()]

WIDTH, HEIGHT = len(grid[0]), len(grid)


def height(i, j):
    c = grid[j][i]
    return ascii_letters.index({"S": "a", "E": "z"}.get(c, c))


def shortest(start):
    visited = {start}
    stack = [(start,)]
    while stack:
        path = stack.pop(0)
        i, j = path[-1]
        for i_, j_ in ((i-1, j), (i+1, j), (i, j-1), (i, j+1)):
            if 0 <= i_ < WIDTH and 0 <= j_ < HEIGHT and height(i_, j_) <= height(i, j) + 1:
                if grid[j_][i_] == "E":
                    return len(path)
                elif (i_, j_) not in visited:
                    visited.add((i_, j_))
                    stack.append(path + ((i_, j_),))


# part 1
print(shortest(next((i, j) for i in range(WIDTH) for j in range(HEIGHT) if grid[j][i] == "S")))

# part 2
print(min(filter(None, (shortest((i, j)) for i in range(WIDTH) for j in range(HEIGHT) if grid[j][i] == "a"))))
