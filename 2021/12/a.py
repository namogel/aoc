from collections import Counter

map_ = {}
with open("input") as fd:
    for line in fd.readlines():
        a, b = line.strip().split("-")
        map_.setdefault(a, []).append(b)
        map_.setdefault(b, []).append(a)


def next_(path):
    p = path[-1]
    if p == "end":
        return [path]

    small_twice = any(
        c > 1
        for c in Counter(
            r for r in path if r != "start" and r == r.lower()
        ).values()
    )

    res = []
    for n in map_[p]:
        if n != "start" and (n == n.upper() or n not in path or not small_twice):
            res.extend(next_(path[:] + [n]))
    return res


print(len(next_(["start"])))
