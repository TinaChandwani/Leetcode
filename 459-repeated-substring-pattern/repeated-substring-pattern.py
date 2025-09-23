class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        # Applying KMP algorithm
        m = len(s)
        i = 1
        prev = 0
        lps = [0] * m
        while i < m:
            if s[i] == s[prev]:
                lps[i] = prev + 1
                prev += 1
                i += 1
            else:
                if prev == 0:
                    lps[i] = 0
                    i += 1
                else:
                    prev = lps[prev-1]
        k = lps[-1]
        to_check = m - k
        if k > 0:
            if m % to_check == 0:
                return True
        return False