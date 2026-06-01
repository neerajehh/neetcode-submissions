"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        clones = {}
        if not node:
         return None
        clones[node] = Node(node.val)
        queue = [node]
        while queue: 
         current = queue.pop(0)
         for x in current.neighbors:
            if x not in clones: 
               clones[x] =   Node(x.val)
               queue.append(x)
            clones[current].neighbors.append(clones[x])
        return clones[node]

