class Solution:
    def longestPrefix(self, s: str) -> str:
        '''
        This I am relating with KMP algorithm LPS array creation
        '''
        m = len(s)
        if m == 0:
            return ""
        lps = [0] * m
        i = 1
        prev = 0
        while i < m:
            if s[i] == s[prev]:
                lps[i] = prev + 1
                prev += 1
                i += 1
            elif prev == 0:
                lps[i] = 0
                i += 1
            else:
                prev = lps[prev-1]
        return s[:lps[-1]]