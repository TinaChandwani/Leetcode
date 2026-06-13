class TrieNode:
    def __init__(self):
        self.w = ""
        self.children = {}
        self.endWord = False

class Solution:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self,words):
        for word in words:
            curr = self.root
            for i in word:
                if i not in curr.children:
                    curr.children[i] = TrieNode()
                curr = curr.children[i]
            curr.w = word
            curr.endWord = True

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        '''
        Brute Force : for every word do a DFS search
        It's very costly
        worst case = mn * 4^mn [ 4 because of all directions] -> this is for 1 word
        '''
        # Create a Trie with words 
        self.insert(words)
        n = len(board)
        m = len(board[0])
        visit = set()
        ans = set()

        def dfs(r,c,node):
            if r < 0  or r >= n or c <0 or c >= m or (r,c) in visit or board[r][c] not in node.children:
                return
            
            visit.add((r,c))
            node = node.children[board[r][c]]

            if node.endWord:
                ans.add(node.w)
            
            dfs(r+1,c,node)
            dfs(r-1,c,node)
            dfs(r,c+1,node)
            dfs(r,c-1,node)

            visit.remove((r,c))

        for i in range(n):
            for j in range(m):
                dfs(i,j,self.root)
        
        return list(ans)
