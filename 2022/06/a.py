with open("input") as fd:
    line = fd.readlines()[0].rstrip("\n")

# n = 4  # part 1
n = 14  # part 2
print(next(i + n for i in range(len(line) - n) if len(set(line[i:i+n])) == n))
