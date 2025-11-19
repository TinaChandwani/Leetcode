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
        Solved using BFS
        Time Complexity -  O(V + E) (no matter the type of graph)= you visit every node once -> V and you look
        at every edge once -> E

        Sparse Graph -> 
            -> Very few edges so E ~ V - 1 so runtime is closer to O(V)
        Dense Graph ->
            -> Almost every node is connected to every other node
            -> E ~ V^2 so runtime is O(V^2)
        Tree ->
            -> No cycles - each node has 1 parent except the root
            -> E = V - 1 => Runtime O(V)
        Fully Connected Graph ->
            -> Each node has edges to all others
            -> E = V (V-1) => Runtime O(V^2)

        Space Complexity -  O(V) = clones stores one cloned node per original
        and visit also stores upto V nodes
        '''
        if not node:
            return None
        q = deque()
        # Create a cloned graph which will have the ans
        clones = {}
        clones[node] = Node(node.val) # Clone the starting node
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
        return clones[node] # Return the cone that matches starting node
            
