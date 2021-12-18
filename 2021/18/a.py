from functools import reduce

NOT_NUMBER = {"[", "]", ","}

with open("input") as fd:
    lines = [l.strip() for l in fd.readlines()]


def explode(v, i):
    start = i
    if v[i+2] in NOT_NUMBER:
        left = int(v[i+1])
        i += 2
    else:
        left = int(v[i+1] + v[i+2])
        i += 3
    if v[i+2] in NOT_NUMBER:
        right = int(v[i+1])
        i += 2
    else:
        right = int(v[i+1] + v[i+2])
        i += 3

    b = []
    for j in range(start-1, -1, -1):
        c = v[j]
        if c in NOT_NUMBER:
            b.append(c)
        else:
            if j > 0 and v[j-1] not in NOT_NUMBER:
                val = int(v[j-1] + v[j])
                j -= 1
            else:
                val = int(v[j])
            result = v[:j] + str(left + val) + "".join(reversed(b))
            break
    else:
        result = "".join(reversed(b))

    result += "0"
    for j in range(i+1, len(v)):
        c = v[j]
        if c in NOT_NUMBER:
            result += c
        else:
            if j < len(v) - 1 and v[j+1] not in NOT_NUMBER:
                val = int(v[j] + v[j+1])
                j += 1
            else:
                val = int(v[j])
            result += str(right + val) + v[j+1:]
            break

    return red(result)


def split(v):
    for i in range(len(v) - 1):
        if v[i] not in NOT_NUMBER and v[i+1] not in NOT_NUMBER:
            n = int(v[i] + v[i+1])
            return red(v[:i] + f"[{n//2},{n//2+n%2}]" + v[i+2:])

    return v


def red(v):
    d = 0
    for i in range(len(v)):
        if v[i] == "[":
            d += 1
        elif v[i] == "]":
            d -= 1
        if d == 5:
            return explode(v, i)

    return split(v)


def add(v1, v2):
    return red(f"[{v1},{v2}]")


def parse(v):
    if len(v) == 1:
        return int(v)

    v = v[1:-1]
    d = 0
    for i in range(len(v)):
        if v[i] == "[":
            d += 1
        elif v[i] == "]":
            d -= 1
        if d == 0:
            return parse(v[:i+1]), parse(v[i+2:])


def magnitude(v):
    if type(v) == int:
        return v
    else:
        return 3 * magnitude(v[0]) + 2 * magnitude(v[1])


def part1():
    return magnitude(parse(reduce(add, lines)))


def part2():
    return max(magnitude(parse(add(n1, n2))) for n1 in lines for n2 in lines if n1 != n2)
