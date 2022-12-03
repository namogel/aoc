from collections import defaultdict

i = 0
calories = defaultdict(int)

with open("input") as fd:
    for line in fd.readlines():
        line = line.strip("\n")
        if line:
            calories[i] += int(line)
        else:
            i += 1

# part 1
print(max(calories.values()))

# part 2
print(sum(sorted(calories.values())[-3:]))
