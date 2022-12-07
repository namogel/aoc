class Node:
    def __init__(self, name, is_dir, parent, size):
        self.name = name
        self.is_dir = is_dir
        self.parent = parent
        self._size = size
        self.children = []

    @property
    def size(self):
        if self._size is None:
            self._size = sum(c.size for c in self.children)
        return self._size


root = Node("/", True, None, None)

with open("input") as fd:
    for line in fd.readlines():
        line = line.rstrip("\n")
        if line.startswith("$ cd"):
            to_ = line[5:]
            if to_ == "/":
                current = root
            elif to_ == "..":
                current = current.parent
            else:
                current = next(c for c in current.children if c.name == to_)
        elif line != "$ ls":
            parts = line.split()
            if parts[0] == "dir":
                child = Node(parts[1], True, current, None)
            else:
                child = Node(parts[1], False, current, int(parts[0]))
            current.children.append(child)


def visit(node):
    if node.is_dir:
        directories.add(node)
        for child in node.children:
            visit(child)


directories = set()
visit(root)

# part 1
print(sum(d.size for d in directories if d.size < 100000))

# part 2
available = 70000000 - root.size
missing = 30000000 - available
print(min(d.size for d in directories if d.size > missing))
