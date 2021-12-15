from heapq import heappush, heappop

with open("input") as fd:
    grid_ = [list(map(int, line.strip())) for line in fd.readlines()]

N = 5
width, height = len(grid_[0]), len(grid_)
full_width, full_height = N * width, N * height


def grid(_j, _i):
    _j, oj = _j % height, _j // height
    _i, oi = _i % width, _i // width
    v = (grid_[_j][_i] + oj + oi)
    return v if v < 10 else 1 + v % 10


visited = set()
j, i = 0, 0
weights = {(j, i): 0}
heap = []
while True:
    for (j_, i_) in ((j, i - 1), (j, i + 1), (j - 1, i), (j + 1, i)):
        if 0 <= j_ < full_height and 0 <= i_ < full_width and (j_, i_) not in visited:
            if (j_, i_) not in weights or weights[(j, i)] + grid(j_, i_) < weights[(j_, i_)]:
                w = weights[(j, i)] + grid(j_, i_)
                weights[(j_, i_)] = w
                heappush(heap, (w, j_, i_))
    visited.add((j, i))
    weight, j, i = heappop(heap)
    if j == full_height - 1 and i == full_width - 1:
        break

print(weight)
