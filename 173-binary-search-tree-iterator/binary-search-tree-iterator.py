# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    '''
    Basically Here simply we need to implement inorder traversal using stack data struture
    One Approach -> Write the inorder traversal of the graph and store it in the list whenever you call next() just print the next element from the list if hasNext() is call just check if are calling the last element from the list then return False else true
    But in this apporach the time and space complexity would be O(1) and O(N) respectively
    Second Approach -> using stack and push all the left nodes until you come accross the root then push all the left nodes of the right and go on -> here since we just pushing the left nodes the space complexity is O(H) where H is the height of the tree
    '''

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self.pushAll(root)
        

    def next(self) -> int:
        # Write the inorder traversal
        stackTop = self.stack.pop()
        if stackTop.right:
            self.pushAll(stackTop.right)
        return stackTop.val

        

    def hasNext(self) -> bool:
        if len(self.stack) != 0:
            return True
        else:
            return False
        
    def pushAll(self,node):
        while node:
            self.stack.append(node)
            node = node.left
         

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()