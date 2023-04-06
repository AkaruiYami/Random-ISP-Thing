from collections import deque
from dataclasses import dataclass


@dataclass
class Node:
    label: str
    value: int

    def __lt__(self, other: "Node"):
        return self.value < other.value

    def __le__(self, other: "Node"):
        return self.value <= other.value

    def __eq__(self, other: "Node"):
        if not isinstance(other, Node):
            return False
        return self.label == other.label and self.value == other.value

    def __ne__(self, other: "Node"):
        if not isinstance(other, Node):
            return True
        return self.label != other.label or self.value != other.value

    def __gt__(self, other: "Node"):
        return self.label > other.label

    def __ge__(self, other: "Node"):
        return self.label >= other.label

    def __str__(self) -> str:
        return self.label + str(self.value)

    def __repr__(self) -> str:
        return self.label + str(self.value)

    def __hash__(self) -> int:
        return hash(self.label + str(self.value))


graph_map = dict[Node, list[Node]]


def best_first_search(graph: graph_map, start_node: Node, goal: Node = None):
    node = ""
    opened = [start_node]
    closed = deque([])
    print(node, list(opened), list(closed), sep="|")
    while opened and node != goal:
        node = opened.pop(0)
        new_nodes = graph.get(node)
        closed.appendleft(node)
        if new_nodes:
            opened.extend(new_nodes)
            opened.sort()
        print(node, list(opened), list(closed), sep="|")
        if node == goal:
            print("Goal reached!")
            break
    else:
        print("Unable to reach the goal!")


A = Node("A", 8)
B = Node("B", 6)
C = Node("C", 7)
D = Node("D", 5)
E = Node("E", 2)
F = Node("F", 3)
G = Node("G", 8)
H = Node("H", 6)
I = Node("I", 11)
J = Node("J", 9)
K = Node("K", 7)
L = Node("L", 3)
M = Node("M", 2)
N = Node("N", 8)
O = Node("O", 10)
P = Node("P", 2)
Q = Node("Q", 0)

goal = Node("Q", 0)

graph = {
    A: [B, C],
    B: [D, E],
    D: [I],
    I: [O],
    E: [J, K],
    C: [F, G, H],
    F: [L, M],
    L: [P],
    M: [Q],
    H: [N],
}

best_first_search(graph, A, goal)
