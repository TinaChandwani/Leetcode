# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val == root.val or q.val == root.val:
            return root
        if (p.val < root.val and q.val > root.val) or (p.val > root.val and q.val < root.val):
            # p and q in different sub trees -> ans will be root
            return root
        elif p.val < root.val and q.val < root.val:
            # Both in left subtree
            return self.lowestCommonAncestor(root.left,p,q)
        else:
            return self.lowestCommonAncestor(root.right,p,q)