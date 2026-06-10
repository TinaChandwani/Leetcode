class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        count = float('inf')
        memo = {}

        def dp(i, j):
            if i == len(word1):
                return (len(word2) - j) # insertions
            
            if j == len(word2):
                return (len(word1) - i)  # deletions
            
            if (i,j) in memo:
                return memo[(i,j)]
            
            if word1[i] == word2[j]:
                memo[(i,j)] = dp(i + 1, j + 1)
            else:

                # Perfom all operations

                # insert
                c = 1 + dp(i, j + 1)

                # delete
                c1 = 1 + dp(i + 1, j)

                # replace
                c2 = 1 + dp(i + 1, j + 1)
                memo[(i,j)] = min(c,c1,c2)
                
            return memo[(i,j)]

        return dp(0, 0)
