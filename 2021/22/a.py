def range_(a, b):
    a = max(a, -50)
    b = min(b, 50)
    return a, b+1


with open("input") as fd:
    instructions = [line.strip() for line in fd.readlines()]


def part1():
    cube = [[[0 for _ in range(101)] for _ in range(101)] for _ in range(101)]
    for i, instruction in enumerate(instructions):
        if instruction.startswith("on"):
            v = 1
            instruction = instruction[3:]
        else:
            v = 0
            instruction = instruction[4:]
        xr, yr, zr = (range_(*map(int, r[2:].split(".."))) for r in instruction.split(","))
        for z in range(*zr):
            for y in range(*yr):
                for x in range(*xr):
                    cube[50+z][50+y][50+x] = v
        print(sum(sum(sum(row) for row in grid) for grid in cube))


def inter(a_min, a_max, b_min, b_max):
    assert a_min <= a_max and b_min <= b_max
    if a_min > b_max or  a_max < b_min:
        return None
    else:
        return max(a_min, b_min), min(a_max, b_max)


def get_count(xr, yr, zr):
    return (zr[1] - zr[0]) * (yr[1] - yr[0]) * (xr[1] - xr[0])


class Cube:
    def __init__(self, xr, yr, zr):
        self.xr = xr
        self.yr = yr
        self.zr = zr
        self.off = []
        self.count = get_count(xr, yr, zr)

    def __contains__(self, other):
        return all(
            self_min <= other_min and self_max >= other_max
            for ((self_min, self_max), (other_min, other_max)) in zip(
                (self.xr, self.yr, self.zr), (other.xr, other.yr, other.zr)
            )
        )

    # def on(self, xr_, yr_, zr_):
    #     intersection = [
    #         inter(*self_cr, other_cr)
    #         for (self_cr, other_cr) in zip((self.xr, self.yr, self.zr), (xr_, yr_, zr_))
    #     ]
    #     if not all(intersection):
    #         return
    #
    #     self.off.append(intersection)
    #     self.count -= get_count(*intersection)

    def off(self, xr_, yr_, zr_):
        intersection = [
            inter(*self_cr, other_cr)
            for (self_cr, other_cr) in zip((self.xr, self.yr, self.zr), (xr_, yr_, zr_))
        ]
        if not all(intersection):
            return

        self.off.append(intersection)
        self.count -= get_count(*intersection)


cubes = []
for instruction in instructions:
    if instruction.startswith("on"):
        cubes.append()