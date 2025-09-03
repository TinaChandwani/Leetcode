# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        _maxSum = -999999

        def pathTraversal(node):
            currVal = 0
            if node == None:
                return 0
            
            # left sub tree
            lt = max(0, pathTraversal(node.left))
            # right sub tree
            rt = max(0, pathTraversal(node.right))

            currVal = node.val+lt+rt
            nonlocal _maxSum
            _maxSum = max(_maxSum, currVal, node.val+lt, node.val+rt)

            return max(node.val+lt, node.val+rt)
        
        pathTraversal(root)

        return _maxSum