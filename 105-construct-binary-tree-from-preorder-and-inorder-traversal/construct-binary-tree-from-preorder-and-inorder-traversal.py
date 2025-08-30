# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder and not inorder:
            return None

        bDict = {i:v for v,i in enumerate(inorder)}
        def helper(preorder,preStart,preEnd,inorder,inStart,inEnd,bDict):
            if preStart > preEnd or inStart > inEnd:
                return None
            root = TreeNode(preorder[preStart])
            inRoot = bDict[root.val]
            numsLeft = inRoot - inStart

            root.left = helper(preorder, preStart + 1,preStart + numsLeft , inorder, inStart, inRoot - 1,bDict)
            root.right = helper(preorder, preStart + numsLeft + 1, preEnd, inorder, inRoot + 1, inEnd, bDict)
            return root
        
        root = helper(preorder, 0, len(preorder) - 1 , inorder, 0, len(inorder) - 1, bDict)
        return root

             