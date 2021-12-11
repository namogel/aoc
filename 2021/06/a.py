from collections import Counter

with open("input") as fd:
    for line in fd.readlines():
        fishes = Counter(map(int, line.split(",")))

for day in range(256):
    new_fishes = Counter()
    for d, c in fishes.items():
        if d == 0:
            new_fishes[6] += c
            new_fishes[8] += c
        else:
            new_fishes[d - 1] += c
    fishes = new_fishes

print(sum(fishes.values()))
