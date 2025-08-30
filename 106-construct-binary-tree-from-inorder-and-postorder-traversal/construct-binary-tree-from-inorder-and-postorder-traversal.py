# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder and not postorder:
            return None
        # Convert inorder list to a hashmap for O(1) lookup
        iDict = {i:v for v,i in enumerate(inorder)}

        def helper(postorder, postStart, postEnd, inorder, inStart, inEnd, iDict):
            if postStart > postEnd or inStart > inEnd:
                return None
            root_val = postorder[postEnd]
            root = TreeNode(root_val)
            inRoot  = iDict[root_val]
            numsLeft = inRoot - inStart
            root.left = helper(postorder,postStart,postStart + numsLeft - 1, inorder, inStart,inRoot - 1,iDict)
            root.right = helper(postorder,postStart + numsLeft, postEnd - 1, inorder, inRoot + 1, inEnd,iDict)
            return root
        
        root = helper(postorder, 0, len(postorder)-1, inorder, 0, len(inorder)-1,iDict)
        return root

        