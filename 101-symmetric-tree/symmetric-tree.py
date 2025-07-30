# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        q_left = deque()
        q_right = deque()
        q_left.append(root.left)
        q_right.append(root.right)
        while q_left and q_right:
            ql = q_left.popleft()
            qr = q_right.popleft()
            if not ql and not qr:
                continue
            if not ql or not qr or (ql.val != qr.val):
                return False

            q_left.append(ql.left)
            q_left.append(ql.right)
            q_right.append(qr.right)
            q_right.append(qr.left)
        return True
            





