class Solution:
    def balancedString(self, s: str) -> int:
        bDict = defaultdict(int)
        l = 0
        r = 0
        n = len(s)
        k = n // 4
        count = float('inf')

        for i in s:
            bDict[i] += 1
        
        while r < n:
            bDict[s[r]] -= 1
            while l < n and bDict['Q'] <= k and bDict['W'] <= k and bDict['E'] <= k and bDict['R'] <= k:
                # We have reached a valid case -> Shrink
                count = min(count,r-l+1)
                bDict[s[l]] += 1
                l += 1
            r += 1
        return count