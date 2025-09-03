# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxWidth = 0
        
        q = deque()
        index = 0
        q.append((root, index))

        while q:
            lenQ = len(q)
            for i in range(lenQ):
                curr_node, curr_index = q.popleft()
                if i == 0:
                    first = curr_index
                if i == lenQ-1:
                    last = curr_index
                if curr_node.left:
                    q.append((curr_node.left, curr_index*2 + 1))
                if curr_node.right:
                    q.append((curr_node.right, curr_index*2 + 2))
                maxWidth = max(maxWidth, last-first+1)
        
        return maxWidth
                