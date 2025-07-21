# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
        ans_left = self.isSameTree(p.left,q.left)
        ans_right = self.isSameTree(p.right,q.right)

        if ans_left and ans_right:
            return True
        else:
            return False

        