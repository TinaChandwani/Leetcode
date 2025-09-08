# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        '''
        2 Approaches:
        1) Inorder traversal -> store it in an array -> if the array is sorted then yes it is valid BST else False
        2) Boundaries (left and right)
        '''
        # 1st Approach -> Inorder
        ans = []
        def inorder(node):
            nonlocal ans
            if not node:
                return 
            inorder(node.left)
            ans.append(node.val)
            inorder(node.right)
            return ans
        inorder(root)
        for i in range(len(ans)-1):
            if ans[i+1] <= ans[i]:
                return False
        return True

        