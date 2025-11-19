"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        q = deque()
        # Create a cloned graph which will have the ans
        clones = {}
        clones[node] = Node(node.val)
        q.append(node)
        visit = set()
        while q:
            n = q.popleft()
            for nei in n.neighbors:
                if nei not in visit:
                    clones[nei] = Node(nei.val)
                    q.append(nei)
                    visit.add(nei)
                clones[n].neighbors.append(clones[nei])
        return clones[node]
            
