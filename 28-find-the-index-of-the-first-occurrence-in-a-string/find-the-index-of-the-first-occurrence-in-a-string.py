class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # Naive Approach
        m = len(needle)
        n = len(haystack)
        if m == 0 or n == 0:
            return 0
        if m > n:
            return -1
        for i in range(n):
            if needle[0] == haystack[i]:
                j = i
                while j < n and j < (i + m) and haystack[j] == needle[j-i]:
                    j += 1
                if j-i == m:
                    return i
        return -1

        