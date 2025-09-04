# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def dia(node):
            nonlocal ans
            if not node:
                return 0
            lh = dia(node.left)
            rh = dia(node.right)
            ans = max(ans,lh+rh)
            return max(lh,rh) + 1
        dia(root)
        return ans