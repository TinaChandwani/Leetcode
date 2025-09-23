class Solution:
    def shortestPalindrome(self, s: str) -> str:
        # Using KMP Algorithm
        t = s + "#" + s[::-1]
        m = len(t)
        lps = [0] * m
        prev = 0
        i = 1
        while i < m:
            if t[i] == t[prev]:
                lps[i] = prev + 1
                prev += 1
                i += 1
            else:
                if prev == 0:
                    lps[i] = 0
                    i += 1
                else:
                    prev = lps[prev - 1]
        p = lps[-1]
        return s[p:][::-1] + s
