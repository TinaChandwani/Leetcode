class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        '''
        KMP Algorithm -> O(m+n) Time Complexity
        The two phases/steps to follow :
        1. Create a LPS array (longest prefix suffix array) using pattern (needle)
        2. Using the LPS array solve the problem in linear time
        '''
        m = len(needle)
        n = len(haystack)
        if m == "":
            return 0
        if m > n:
            return -1
        # LPS Array
        i = 1
        lps = [0] * m
        prev = 0
        while i < m:
            if needle[i] == needle[prev]:
                lps[i] = prev + 1
                prev += 1
                i += 1
            elif prev == 0:
                lps[i] = 0
                i += 1
            else:
                prev = lps[prev - 1]
        
        # Linearly
        i = 0
        j = 0
        while i < n:
            if needle[j] == haystack[i]:
                i += 1
                j += 1
            else:
                if j == 0:
                    i += 1
                else:
                    j = lps[j-1]
            if j == m:
                return i - m
        return -1