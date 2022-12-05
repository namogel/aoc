import re

letter = re.compile(r"\w")
move = re.compile(r"move (\d+) from (\d+) to (\d+)")
stacks = [[] for _ in range(10)]

with open("input") as fd:
    for line in fd.readlines():
        line = line.rstrip("\n")
        if not line.startswith(" 1 "):
            for i in range(len(line) // 4 + 1):
                if match := letter.search(line[i*4:i*4+4]):
                    stacks[i + 1].insert(0, match.group())
        if line.startswith("move"):
            count, from_, to_ = map(int, move.search(line).groups())
            # part 1
            # stacks[to_].extend(stacks[from_][-count:][::-1])
            # part 2
            stacks[to_].extend(stacks[from_][-count:])
            stacks[from_] = stacks[from_][:-count]

print("".join(s[-1] for s in stacks[1:]))
