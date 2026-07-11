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
        visit = set()
        res = []


        while curr:
            if curr not in visit:
                visit.add(curr)
                res.append(curr.val)
            if curr.left is None:     
                curr = curr.right
            else:
                leftchild = curr.left
                while leftchild.right:
                    leftchild = leftchild.right
                
                leftchild.right = curr

                # set the node to null
                temp = curr
                curr = curr.left
                temp.left = None
        
        return res

