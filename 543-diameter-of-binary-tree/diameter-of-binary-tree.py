# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_c = 0
        def dfs(root):
            nonlocal max_c
            if not root:
                return 0
            l = dfs(root.left)
            r = dfs(root.right)
            max_c = max(l + r,max_c)
            return max(l,r) + 1 
        dfs(root)
        return max_c       