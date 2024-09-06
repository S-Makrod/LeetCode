from typing import Optional

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        visited = {}
        graph = Node(node.val, None)
        queue = [(node, graph)]

        while queue:
            curr, currCopy = queue.pop(0)
            visited[curr] = currCopy

            for val in curr.neighbors:
                if val not in visited:
                    new = Node(val.val, None)
                    queue.append((val, new))
                    visited[val] = new

                currCopy.neighbors.append(visited[val])

        return graph


