"""Print nodes that have no children and no older sibling."""


class Node:
    def __init__(self, value):
        self.value = value
        self.p1 = None
        self.p2 = None
        self.children = []

    def set_parent(self, p1):
        self.p1 = p1
        if p1.p2 is None:
            p1.p2 = self
        else:
            current = p1.p2
            while current.p2 is not None:
                current = current.p2
            current.p2 = self

        p1.children.append(self)


def print_node_without_parent_sibling(root_node):
    if root_node is None:
        return []

    visited = [root_node]

    while visited:
        current_node = visited.pop()

        has_no_children = len(current_node.children) == 0
        has_no_siblings = (current_node.p1 is None) or (current_node.p1.p2 == current_node)

        if has_no_children and has_no_siblings:
            print(current_node.value)

        for child in current_node.children:
            visited.append(child)


# Create nodes
a = Node("A")
b = Node("B")
c = Node("C")
d = Node("D")
e = Node("E")
f = Node("F")
g = Node("G")
h = Node("H")
i = Node("I")
j = Node("J")
k = Node("K")
l = Node("L")
m = Node("M")
n = Node("N")
o = Node("O")
p = Node("P")

# Set parent-child relationships
b.set_parent(a)
c.set_parent(b)
d.set_parent(c)
e.set_parent(d)
f.set_parent(b)
g.set_parent(f)
h.set_parent(c)
k.set_parent(h)
i.set_parent(d)
j.set_parent(e)
l.set_parent(j)
m.set_parent(l)
n.set_parent(m)
o.set_parent(l)
p.set_parent(o)

print_node_without_parent_sibling(a)
