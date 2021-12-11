aim, x, y = 0, 0, 0
with open("input") as fd:
    for line in fd.readlines():
        inst, value = line.split(" ")
        value = int(value)
        if inst == "forward":
            x += value
            y += value * aim
        elif inst == "down":
            aim += value
        elif inst == "up":
            aim -= value

print(x * y)

