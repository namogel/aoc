with open("input") as fd:
    depths = tuple(map(int, fd.readlines()))

c = 0
p = 158
for d in depths:
    if d > p:
        c += 1
    p = d
print(c)

c = 0
p = sum(depths[:3])
for i in range(len(depths) - 3):
    if sum(depths[i+1:i+4]) > sum(depths[i:i+3]):
        c += 1
print(c)
