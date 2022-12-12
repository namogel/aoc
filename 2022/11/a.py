from functools import reduce


class Monkey:
    def __init__(self, items, operation, d, t, f):
        self.items = items
        self.operation = operation
        self.d = d
        self.t = t
        self.f = f
        self.count = 0


monkeys = [
    Monkey([75, 63], lambda x: 3 * x, 11, 7, 2),
    Monkey([65, 79, 98, 77, 56, 54, 83, 94], lambda x: x + 3, 2, 2, 0),
    Monkey([66], lambda x: x + 5, 5, 7, 5),
    Monkey([51, 89, 90], lambda x: x * 19, 7, 6, 4),
    Monkey([75, 94, 66, 90, 77, 82, 61], lambda x: x + 1, 17, 6, 1),
    Monkey([53, 76, 59, 92, 95], lambda x: x + 2, 19, 4, 3),
    Monkey([81, 61, 75, 89, 70, 92], lambda x: x * x, 3, 0, 1),
    Monkey([81, 86, 62, 87], lambda x: x + 8, 13, 3, 5),
]

# part 1
for j in range(20):
    for monkey in monkeys:
        while monkey.items:
            item = monkey.operation(monkey.items.pop(0)) // 3
            monkeys[monkey.t if not item % monkey.d else monkey.f].items.append(item)
            monkey.count += 1

# part 2
lcm = reduce(lambda x, y: x * y, (m.d for m in monkeys))
for j in range(100000):
    for monkey in monkeys:
        while monkey.items:
            item = monkey.operation(monkey.items.pop(0)) % lcm
            monkeys[monkey.t if not item % monkey.d else monkey.f].items.append(item)
            monkey.count += 1

monkeys.sort(key=lambda m: m.count)
print(monkeys[-2].count * monkeys[-1].count)
