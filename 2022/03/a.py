from string import ascii_letters

priority = 0

# part 1
with open("input") as fd:
    for line in fd.readlines():
        line = line.rstrip("\n")
        assert not len(line) % 2
        mid = len(line) // 2
        common = list(set(line[:mid]) & set(line[mid:]))
        assert len(common) == 1
        priority += ascii_letters.index(common[0]) + 1

# part 2
group = []
with open("input") as fd:
    for line in fd.readlines():
        line = line.rstrip("\n")
        group.append(set(line))
        if len(group) < 3:
            continue
        common = list(set.intersection(*group))
        assert len(common) == 1
        priority += ascii_letters.index(common[0]) + 1
        group = []

print(priority)
