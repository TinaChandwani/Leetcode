class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        '''
        Bottom Up Approach
        t[i][j]:- longest common subsequence between s1 of len i and s2 of len j
        i , j are length not index, that's how we have defined it
        '''
        m = len(text1)
        n = len(text2)
        t = [[0 for _ in range(n + 1)] for k in range(m + 1)]

        for i in range(1,m + 1):
            for j in range(1,n + 1):
                if text1[i-1] == text2[j-1]:
                    t[i][j] = 1 + t[i-1][j-1]
                else:
                    t[i][j] = max(t[i][j-1],t[i-1][j])
        
        return t[m][n]