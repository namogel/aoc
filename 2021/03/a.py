with open("input") as fd:
    lines = [line.rstrip("\n") for line in fd]


def mc(i):
    return "1" if counts[i]["1"] >= counts[i]["0"] else "0"


def lc(i):
    return "0" if counts[i]["1"] >= counts[i]["0"] else "1"


counts = {}
for l in lines:
    for i, v in enumerate(l):
        counts.setdefault(i, {"0": 0, "1": 0})[v] += 1

gamma = "".join(mc(i) for i in range(len(lines[0])))
epsilon = "".join(lc(i) for i in range(len(lines[0])))
print(int(gamma, 2) * int(epsilon, 2))

oxygen = list(lines)
k = 0
while len(oxygen) > 1:
    counts = {}
    for l in oxygen:
        for i, v in enumerate(l):
            counts.setdefault(i, {"0": 0, "1": 0})[v] += 1
    for i, line in reversed(list(enumerate(oxygen))):
        if line[k] != mc(k):
            oxygen.pop(i)
    k += 1


co2 = list(lines)
k = 0
while len(co2) > 1:
    counts = {}
    for l in co2:
        for i, v in enumerate(l):
            counts.setdefault(i, {"0": 0, "1": 0})[v] += 1
    for i, line in reversed(list(enumerate(co2))):
        if line[k] != lc(k):
            co2.pop(i)
    k += 1


print(int(oxygen[0], 2) * int(co2[0], 2))
