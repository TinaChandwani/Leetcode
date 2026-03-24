class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        cDict = defaultdict(int)
        n = len(s)
        l = 0
        r = 0
        count = 0

        while r < n:
            cDict[s[r]] += 1
            while len(cDict) == 3:
                # valid window
                count += (n-r)
                cDict[s[l]] -= 1
                if cDict[s[l]] == 0:
                    del cDict[s[l]]
                l += 1
            r += 1
        
        return count