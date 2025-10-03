# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        '''
        Key Observations:
        1) Inorder of a BST is sorted
        2) Balance comes from choosing near the middle as root, so left and right sizes are of similar sizes ==> This is important because we need a height balanced tree
        So basically, do binary search 
        '''
        if not nums:
            return 
        def build(l,r):
            if l >= r:
                return None
            mid = (l+r) // 2        
            node = TreeNode(nums[mid])
            node.left = build(l,mid)
            node.right = build(mid+1,r)
            return node
        return build(0,len(nums))
