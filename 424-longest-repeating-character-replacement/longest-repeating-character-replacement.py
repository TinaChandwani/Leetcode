class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        l = 0
        r = 0
        maxFreq = 0
        sDict = defaultdict(int)
        maxLen = 0

        while r < n:
            sDict[s[r]] += 1
            maxFreq = max(maxFreq,sDict[s[r]])
            while (r - l + 1) - maxFreq > k:
                # Shrink
                sDict[s[l]] -= 1
                l += 1
            maxLen = max(maxLen,r-l+1)
            r += 1
        return maxLen
