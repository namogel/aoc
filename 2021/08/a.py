from collections import defaultdict


def o(s):
    if isinstance(s, set):
        assert len(s) == 1
        return s.pop()
    else:
        r = list(s)
        assert len(r) == 1
        return r[0]


NUMBERS = {
    "abcefg": 0,
    "cf": 1,
    "acdeg": 2,
    "acdfg": 3,
    "bcdf": 4,
    "abdfg": 5,
    "abdefg": 6,
    "acf": 7,
    "abcdefg": 8,
    "abcdfg": 9,
}

with open("input") as fd:
    res = 0
    for line in fd:
        m = {}
        inputs, outputs = [p.split(" ") for p in line.strip().split(" | ")]
        digits = defaultdict(set)
        for i in inputs:
            digits[len(i)].add(i)

        one = set(o(digits[2]))
        four = set(o(digits[4]))
        seven = set(o(digits[3]))
        height = set(o(digits[7]))
        m["a"] = o(seven - one)
        horizontals = set.intersection(*[set(d) for d in digits[5]])
        m["g"] = o(horizontals - four - {m["a"]})
        m["d"] = o(horizontals - {m["a"], m["g"]})
        m["b"] = o(four - {m["d"]} - one)
        five = set(o(d for d in digits[5] if m["b"] in d))
        m["f"] = o(five - horizontals - {m["b"]})
        m["c"] = o(one - {m["f"]})
        m["e"] = o(height - set(m.values()))
        m = {v: k for k, v in m.items()}

        res += int("".join(str(NUMBERS["".join(sorted(m[c] for c in output))]) for output in outputs))

print(res)
