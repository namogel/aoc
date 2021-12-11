CHARS = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">"
}
SCORES = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4,
}
scores = []
with open("input") as fd:
    for line in fd.readlines():
        stack = []
        is_corrupt = False
        for c in line.strip():
            if c in CHARS:
                stack.append(c)
                continue
            if c != CHARS[stack.pop()]:
                is_corrupt = True
                break
        if not is_corrupt:
            score = 0
            while stack:
                score = 5 * score + SCORES[CHARS[stack.pop()]]
            scores.append(score)

scores.sort()
print(scores[int(len(scores)/2)])
