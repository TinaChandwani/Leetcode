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
        def dfs(left,right):
            if not left and not right:
                return True
            if not left or not right or left.val != right.val:
                return False
            
            l = dfs(left.right,right.left)
            r = dfs(left.left, right.right)
            return l and r
        
        return dfs(root.left,root.right)
