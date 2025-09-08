# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        good = 0
        def travese(node,maxPath):
            nonlocal good
            if not node:
                return
            if maxPath <= node.val:
                good += 1
                maxPath = node.val
            travese(node.left,maxPath)
            travese(node.right,maxPath)
            return good
        # if root.left:
        #     nl = travese(root.left,root.val)
        # if root.right:
        #     nr = travese(root.right,root.val)
        # return nl + nr
        return travese(root,root.val)
        