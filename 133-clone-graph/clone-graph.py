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
        '''
        you need to create a hashmap[original] = clone
        '''
        if not node:
            return None
        adj = {}
        q = deque()
        q.append(node)
        adj[node] = Node(node.val)

        while q:
            n = q.popleft()
            for nei in n.neighbors:
                if nei not in adj:
                    new_node = Node(nei.val)
                    adj[nei] = new_node
                    q.append(nei)
                adj[n].neighbors.append(adj[nei])
        return adj[node]
