class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        '''
        time : O(length of text1 * length of text 2)
        space (length of text1 * length of text 2)
        '''
        # base case
        memo = {}
        def dp(i,j):
            if i == len(text1) or j == len(text2):
                return 0
            
            if (i,j) in memo:
                return memo[(i,j)]
            
            if text1[i] == text2[j]:
                memo[(i,j)] = 1 + dp(i+1,j+1)
            else:
                memo[(i,j)] = max(dp(i+1,j),dp(i,j+1))
            
            return memo[(i,j)]
        
        return dp(0,0)