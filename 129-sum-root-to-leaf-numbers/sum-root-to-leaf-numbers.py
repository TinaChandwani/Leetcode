# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        # Recursive Approach
        def dfs(node,value):
            if not node:
                return 0
            value = value * 10 + node.val
            if not node.left and not node.right:
                return value
            return (dfs(node.left,value) + dfs(node.right,value))
        return dfs(root,0)
    