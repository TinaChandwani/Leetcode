class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        count = float('inf')
        memo = {}

        def dp(i, j, count):
            if i == len(word1):
                return (len(word2) - j) # insertions
            
            if j == len(word2):
                return (len(word1) - i)  # deletions
            
            if word1[i] == word2[j]:
                return dp(i + 1, j + 1,count)
            
            if (i,j) in memo:
                return memo[(i,j)]

            # Perfom all operations

            # insert
            c = 1 + dp(i, j + 1, count + 1)

            # delete
            c1 = 1 + dp(i + 1, j, count + 1)

            # replace
            c2 = 1 + dp(i + 1, j + 1, count + 1)

            ans = min(c,c1,c2)
            memo[(i,j)] = ans

            return ans

        return dp(0, 0, 0)
