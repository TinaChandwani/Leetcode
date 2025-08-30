"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        
        q = deque()
        q.append(root)
        while q:
            lq = len(q)
            dummy = Node(0)
            for i in range(lq):
                node = q.popleft()
                dummy.next = node
                dummy = dummy.next
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return root