def get_digit(line):
    first_digit = next(c for c in line if c.isdigit())
    last_digit = next(c for c in line[::-1] if c.isdigit())
    return int(first_digit + last_digit)


def part1():
    with open("input") as fd:
        return sum(get_digit(line) for line in fd.readlines())


def part2():
    numbers = ("one", "two", "three", "four", "five", "six", "seven", "eight", "nine")
    s = 0
    with open("input") as fd:
        for line in fd.readlines():
            for i, number in enumerate(numbers, 1):
                line = line.replace(number, f"{number[0]}{i}{number[-1]}")
            s += get_digit(line)
    return s
