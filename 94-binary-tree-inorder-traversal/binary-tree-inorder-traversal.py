# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        Morris Algorithm:
        1) Take a curr node :
            -> check if node.left exist then node.left.right and connect with the curr node (root node)
        """
        if root is None:
            return []

        curr = root
        res = []

        while curr is not None:
            if curr.left is None:
                res.append(curr.val)
                curr = curr.right
            else:
                leftchild = curr.left

                while leftchild.right :
                    leftchild = leftchild.right

                leftchild.right = curr

                # curr ka left ko None kar sakte ho
                temp = curr
                curr = curr.left
                temp.left = None

        return res
