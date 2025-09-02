# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        '''
        Basically There are 2 approaches to solve the problem:
        Recursively -> there are chance of running into recursion depth issues
        Iteratively -> using DFS 

        Edge cases:
        If the tree is empty -> return False
        if single node then check root.val == target
        Negative values should not impact the logic
        No partial sums
        '''
        # # Recursive Approach
        # if not root:
        #     return False
        
        # if not root.left and not root.right and root.val == targetSum:
        #     return True
        
        # rem = targetSum - root.val
        # left = self.hasPathSum(root.left,rem)
        # right = self.hasPathSum(root.right,rem)

        # return left or right

        # Iterative Approach using DFS
        if not root:
            return False
        if not root.left and not root.right and root.val == targetSum:
            return True
        q = deque()
        q.append([root,root.val])

        while q:
            node,s = q.popleft()
            if not node.left and not node.right and s == targetSum:
                return True
            if node.left:
                q.append([node.left, s + node.left.val])
            if node.right:
                q.append([node.right, s + node.right.val])
        return False
        