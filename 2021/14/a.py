from collections import Counter
import functools

with open("input") as fd:
    poly, _, *rules = fd.readlines()

poly = poly.strip()
rules = dict(r.strip().split(" -> ") for r in rules)


@functools.cache
def count(p, n):
    if n == 0 or p not in rules:
        return Counter(p[:1])
    else:
        return count(p[0] + rules[p], n - 1) + count(rules[p] + p[1], n - 1)


counter = Counter()
for i in range(len(poly) - 1):
    counter.update(count(poly[i:i+2], 40))
counter += Counter(poly[-1:])

l, *_, m = sorted(counter.values())
print(m - l)
