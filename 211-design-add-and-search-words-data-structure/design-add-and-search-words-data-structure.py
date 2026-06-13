class TrieNode:
    def __init__(self):
        self.children = {}
        self.endWord = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()
        
    def addWord(self, word: str) -> None:
        curr = self.root

        for i in word:
            if i not in curr.children:
                curr.children[i] = TrieNode()
            curr = curr.children[i]
        curr.endWord = True
        

    def search(self, word: str) -> bool:
        def dfs(node,i):
            if i == len(word):
                return node.endWord
            
            ch = word[i]
            
            if ch == '.':
                for child in node.children.values():
                    if dfs(child,i+1):
                        return True
                return False
            else:
                if ch not in node.children:
                    return False
                return dfs(node.children[ch], i +1)
            
        return dfs(self.root,0)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)