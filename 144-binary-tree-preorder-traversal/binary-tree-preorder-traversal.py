# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        '''
        Root -> left -> right
        '''
        if root is None:
            return []
        
        curr = root
        res = []


        while curr:
            res.append(curr.val)
            if curr.left is None:     
                curr = curr.right
            else:
                leftchild = curr.left
                while leftchild.right:
                    leftchild = leftchild.right

                if curr.right:
                    leftchild.right = curr.right
                    # set the node to null
                    temp = curr
                    temp.right = None
                curr = curr.left
                
        return res

