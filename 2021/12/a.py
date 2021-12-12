from typing import List, Dict, Set, NamedTuple


map_: Dict[str, List[str]] = {}
with open("input") as fd:
    for line in fd.readlines():
        a, b = line.strip().split("-")
        map_.setdefault(a, []).append(b)
        map_.setdefault(b, []).append(a)


class Path(NamedTuple):
    rooms: List[str]
    small_twice: bool
    lower: Set


def next_(path: Path) -> List[Path]:
    p = path.rooms[-1]
    if p == "end":
        return [path]

    res = []
    for n in map_[p]:
        if n != "start" and (n.isupper() or n not in path.lower or not path.small_twice):
            res.extend(next_(Path(
                rooms=path.rooms[:] + [n],
                small_twice=path.small_twice or n.islower() and n in path.lower,
                lower=set(path.lower) | ({n} if n.islower() else set())
            )))
    return res


print(len(next_(Path(rooms=["start"], small_twice=False, lower=set()))))
