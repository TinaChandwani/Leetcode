class TrieNode:
    def __init__(self):
        self.children = {}
        self.endWord = False

class Solution:
    def __init__(self):
        self.root = TrieNode()

    def addDigit(self,num):
        s = str(num)
        curr = self.root
        for i in s:
            if i not in curr.children:
                curr.children[i] = TrieNode()
            curr = curr.children[i]
        curr.endWord = True


    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        common = 0
        for n in arr1:
            self.addDigit(n)
        
        for j in arr2:
            s = str(j)
            curr = self.root
            length = 0
            for ch in s:
                if ch not in curr.children:
                    break
                curr = curr.children[ch]
                length += 1 
                common = max(common,length)   
        
        return common


            

        