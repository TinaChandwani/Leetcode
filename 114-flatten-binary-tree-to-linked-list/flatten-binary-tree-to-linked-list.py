# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        Edge Cases:
        1) If the Tree is empty
        2) If it is already a right skewed tree
        3) For Deeper Imbalanced tree -> You will reach recursion max depth so iterative approach is better, Recursive approach is easy to write for smaller trees but a left skewed tree iterative is better will take O(1) space even for million nodes in the tree
        """
        if not root:
            return None
        head = root
        while head:
            if head.left:
                # Check if left node exists of the head
                curr = head.left
                # Find the rightmost node of the curr
                while curr.right:
                    curr = curr.right
                # Attach the right subtree to curr.right
                curr.right = head.right
                # Make the head.left None
                head.right = head.left
                head.left = None
            head = head.right
        return root
        