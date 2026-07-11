# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        '''
        Recursion
        Root -> left -> right
        '''
        if root is None:
            return []
        
        ans = []

        ans.append(root.val)

        if root.left:
            ans.extend(self.preorderTraversal(root.left))
        
        if root.right:
            ans.extend(self.preorderTraversal(root.right))
        
        return ans
        