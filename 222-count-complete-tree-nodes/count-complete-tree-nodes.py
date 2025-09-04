# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        '''
        Edge Cases :
        1) Empty Tree
        2) Single Node
        3) Highly unbalanced but complete tree
        4) Very tall tree
        '''
        if not root:
            return 0
        # Compute hL
        head = root
        head1 = root
        hL,hR = 0,0
        while head:
            head = head.left
            hL += 1
        while head1:
            head1 = head1.right
            hR += 1
        if hL == hR:
            count = (2 ** hL) - 1
        else:
            count = 1 + self.countNodes(root.left) + self.countNodes(root.right)
        return count
