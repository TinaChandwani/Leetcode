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
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None
        head = root
        while head:
            dummy = Node(0)
            tail = dummy
            while head:
                if head.left:
                    tail.next = head.left
                    tail = tail.next
                if head.right:
                    tail.next = head.right
                    tail = tail.next
                head = head.next
            head = dummy.next
        return root
        