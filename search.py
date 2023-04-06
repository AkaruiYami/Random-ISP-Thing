from collections import deque


def bfs(graph: dict, start_node: str, goal: str = None):

    queue = deque([start_node])
    visited = deque([])

    node = ""
    print(" ", list(queue), list(visited), sep="|")
    while queue and node != goal:
        node = queue.popleft()

        if node not in visited:
            visited.appendleft(node)
            queue.extend(graph.get(node, []))
            print(node, list(queue), list(visited), sep="|")


def dfs(graph: dict, start_node: str, goal: str = None):

    queue = deque([start_node])
    visited = deque([])

    node = ""
    print(" ", list(queue), list(visited), sep="|")
    while queue and node != goal:
        node = queue.popleft()

        if node not in visited:
            visited.appendleft(node)
            opened = list(reversed(graph.get(node, [])))
            queue.extendleft(opened)
            print(node, list(queue), list(visited), sep="|")


graph = {
    "A": list("DCEB"),
    "D": ["G"],
    "G": list("LN"),
    "N": list("RQ"),
    "C": ["I"],
    "I": ["K"],
    "E": ["F"],
    "F": ["M"],
    "M": ["S"],
    "B": ["H"],
    "H": list("OP"),
}


bfs(graph, "A", "Q")
