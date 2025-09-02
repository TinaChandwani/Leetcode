# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        '''
        Here We are going to using the levelmorder dfs approach
        The idea is based on indexing the first and last node of each level and maximum width = last - first + 1
        '''
        if not root:
            return 0
        ans = 0
        q = deque()
        q.append([root,0]) # Indexing should start with 0
        while q:
            lenQ = len(q)
            base = q[0][1]
            for i in range(lenQ):
                node, index = q.popleft()
                curr_id = index - base
                if i == 0:
                    first = curr_id
                if i == lenQ - 1:
                    last = curr_id
                if node.left:
                    q.append([node.left, 2 * curr_id + 1])
                if node.right:
                    q.append([node.right, 2 * curr_id + 2])
            ans = max(ans,last - first + 1)
        return ans
                
