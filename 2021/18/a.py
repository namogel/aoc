from functools import reduce


class Node:
    def __init__(self, parent):
        self.parent = parent
        self.pair = None

    def __str__(self):
        return f"[{','.join(map(str, self.pair))}]"


def get_child_explode(node, depth=4):
    if type(node) == int:
        return None

    if depth == 1:
        for child in node.pair:
            if type(child) == Node:
                return child
        return None

    child_a, child_b = node.pair
    return get_child_explode(child_a, depth - 1) or get_child_explode(child_b, depth - 1)


def get_child_split(node):
    for child in node.pair:
        if type(child) == int:
            if child >= 10:
                return node
        else:
            cs = get_child_split(child)
            if cs:
                return cs

    return None


def explode(node):
    left = node.parent
    while left.parent and left == left.parent.pair[0]:
        left = left.parent
    if left.parent:
        # while type(left.pair[0]) != int:
        # while left.parent and type(left.parent.pair[0]) != int:
        #     left = left.parent
        # if left.parent:
        #     left.pair[0] += node.pair[0]
        raise ValueError

    right = node.parent
    while type(right.pair[0]) != int:
        right = right.pair[0]
    right.pair[0] += node.pair[1]

    if node == node.parent.pair[0]:
        node.parent.pair[0] = 0
    elif node == node.parent.pair[1]:
        node.parent.pair[1] = 0
    else:
        raise ValueError


def split(node):
    for i, child in enumerate(node.pair):
        if type(child) == int and child >= 10:
            node.pair[i] = Node(node)
            node.pair[i].pair = [child // 2, child // 2 + child % 2]
            break


def red(parent):
    node = get_child_explode(parent)
    if node:
        explode(node)
        return red(parent)

    node = get_child_split(parent)
    if node:
        split(node)
        return red(parent)

    return parent


def parse(v, parent=None):
    if len(v) == 1:
        return int(v)

    v = v[1:-1]
    d = 0
    for i in range(len(v)):
        if v[i] == "[":
            d += 1
        elif v[i] == "]":
            d -= 1
        if d == 0:
            node = Node(parent)
            node.pair = [parse(v[:i+1], node), parse(v[i+2:], node)]
            return node


def add(n1, n2):
    node = Node(None)
    node.pair = [n1, n2]
    return red(node)


def magnitude(node):
    if type(node) == int:
        return node
    else:
        return 3 * magnitude(node.pair[0]) + 2 * magnitude(node.pair[1])


def part1():
    return magnitude(reduce(add, lines))


def part2():
    return max(magnitude(add(n1, n2)) for n1 in lines for n2 in lines if n1 != n2)


with open("input") as fd:
    lines = [parse(l.strip()) for l in fd.readlines()]

# print(part1())
# print(part2())


def d(s):
    return str(explode(get_child_explode(parse(s))))


assert d("[[[[[9,8],1],2],3],4]") == "[[[[0,9],2],3],4]"
