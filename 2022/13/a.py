from functools import cmp_to_key

with open("input") as fd:
    lists = [eval(line.rstrip("\n")) for line in fd.readlines() if line.startswith("[")]


def cmp(i1, i2):
    if isinstance(i1, int) and isinstance(i2, int):
        return i1 - i2
    i1 = i1 if isinstance(i1, list) else [i1]
    i2 = i2 if isinstance(i2, list) else [i2]
    for e1, e2 in zip(i1, i2):
        if (io := cmp(e1, e2)) != 0:
            return io
    return len(i1) - len(i2)


# part 1
print(sum(i//2 + 1 for i in range(0, len(lists), 2) if cmp(lists[i], lists[i+1]) <= 0))

# part 2
l1, l2 = [[2]], [[6]]
lists += [l1, l2]
lists.sort(key=cmp_to_key(cmp))
print((lists.index(l1) + 1) * (lists.index(l2) + 1))
