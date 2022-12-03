with open("input") as fd:
    enhancement, _, *grid = fd.readlines()

grid = [row.strip() for row in grid]


def oob():
    return {0: ".", 1: "#"}[n % 2]


def enhance(j, i):
    square = ""
    for j_ in (j-1, j, j+1):
        for i_ in (i-1, i, i+1):
            try:
                square += grid[j_][i_]
            except IndexError:
                square += oob()
    return enhancement[int(square.replace(".", "0").replace("#", "1"), 2)]


for n in range(50):
    width, height = len(grid[0]) + 2, len(grid) + 2
    grid = [oob() * width] + [(oob() + row + oob()) for row in grid] + [oob() * width]
    grid = ["".join(enhance(j, i) for i in range(width)) for j in range(height)]

print(sum(row.count("#") for row in grid))
