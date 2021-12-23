from itertools import permutations


def distance(p1, p2):
    x1, y1, z1 = p1
    x2, y2, z2 = p2
    return (x2-x1) ** 2 + (y2-y1) ** 2 + (z2-z1) ** 2


def distances(points):
    result = {}
    for i in range(len(points)):
        p1 = points[i]
        for j in range(i+1, len(points)):
            p2 = points[j]
            d = distance(p1, p2)
            assert d not in result
            result[d] = (p1, p2)
    return result


def transpose(x, y, z, orientation):
    return tuple(
        {"x": x, "-x": -x, "y": y, "-y": -y, "z": z, "-z": -z}[o]
        for o in orientation
    )


def find_coords(p1, p2, orientation, sign):
    x1, y1, z1 = p1
    x2, y2, z2 = transpose(*p2, orientation)
    return x1 + sign * x2, y1 + sign * y2, z1 + sign * z2


def all_coords(p1, p2):
    coords = {}
    for x in ("x", "-x"):
        for y in ("y", "-y"):
            for z in ("z", "-z"):
                for o in permutations([x, y, z], 3):
                    coords[o] = find_coords(p1, p2, o, -1)

    return coords


def one(it):
    values = list(it)
    if values:
        assert len(values) == 1
        return values[0]


def find_positions():
    while len(positions) < len(scanners) - 1:
        for sf, scanner_from in enumerate(scanners):
            if sf != 0 and sf not in positions:
                continue

            d1 = distances(scanner_from)
            for st, scanner_to in enumerate(scanners):
                if st == 0 or st == sf or st in positions:
                    continue

                d2 = distances(scanner_to)
                inter = list(set(d1.keys()) & set(d2.keys()))
                if len(inter) < 10:
                    continue

                same = {}
                for i1 in range(len(inter) - 1):
                    for i2 in range(i1 + 1, len(inter)):
                        k1, k2 = inter[i1], inter[i2]
                        p1 = one(p for p in scanner_from if (list(d1[k1]) + list(d1[k2])).count(p) == 2)
                        p2 = one(p for p in scanner_to if (list(d2[k1]) + list(d2[k2])).count(p) == 2)
                        if p1 and p2:
                            if p1 in same:
                                assert same[p1] == p2
                            else:
                                same[p1] = p2

                same = list(same.items())
                coords = all_coords(*same[0])
                for p1, p2 in same[1:]:
                    for orientation, coords_ in list(coords.items()):
                        if find_coords(p1, p2, orientation, -1) not in coords.values():
                            coords.pop(orientation)

                assert len(coords) == 1

                ot, pt = list(coords.items())[0]
                if sf != 0:
                    sf_, of, pf = positions[sf]
                    assert sf_ == 0
                    pt = find_coords(pf, pt, of, 1)
                    ot = tuple(
                        {
                            "x": ot[0], "-x": "-" + ot[0], "y": ot[1], "-y": "-" + ot[1], "z": ot[2], "-z": "-" + ot[2]
                        }[o].replace("--", "")
                        for o in of
                    )

                positions[st] = (0, ot, pt)


def part1():
    all_beacons = set(scanners[0])
    for s, beacons in enumerate(scanners[1:], start=1):
        _, o, p = positions[s]
        all_beacons.update(map(lambda b: find_coords(p, b, o, 1), beacons))

    return len(all_beacons)


def part2():
    return max(
        abs(x2 - x1) + abs(y2 - y1) + abs(z2 - z1)
        for _, _, (x1, y1, z1) in positions.values()
        for _, _, (x2, y2, z2) in positions.values()
    )


scanners = []
with open("input") as fd:
    for line in fd.readlines():
        line = line.strip()
        if line.startswith("---"):
            scanner = []
        elif line:
            scanner.append(tuple(map(int, line.split(","))))
        else:
            scanners.append(scanner)
    scanners.append(scanner)

positions = {}
find_positions()
print(part1())
print(part2())
