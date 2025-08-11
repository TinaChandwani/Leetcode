class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # Same as Genetic Mutation problem
        # We will use BFS here

        wordList = set(wordList)
        if endWord not in wordList:
            return 0
        
        q = deque()
        visit = set(beginWord)
        q.append([beginWord,0]) # [word,number of seq]

        while q:
            word,seq = q.popleft()
            if word == endWord:
                return seq + 1
            # Find the next word
            for i in range(len(word)):
                for letter in range(ord('a'),ord('z') + 1):
                    new_word = word[:i] + chr(letter) + word[i+1:]
                    if new_word in wordList and new_word not in visit:
                        q.append([new_word,seq+1])
                        visit.add(new_word)
        return 0