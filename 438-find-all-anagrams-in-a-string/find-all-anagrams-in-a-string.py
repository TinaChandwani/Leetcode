class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        aDict = defaultdict(int)
        pDict = defaultdict(int)
        n = len(s)
        k = len(p)
        ans = []
        l = 0
        r = 0
        
        for i in p:
            pDict[i] += 1

        while r < n:
            aDict[s[r]] += 1
            if r - l + 1 > k:
                aDict[s[l]] -= 1
                if aDict[s[l]] == 0:
                    del aDict[s[l]]
                l += 1
            if r - l + 1 == k and aDict == pDict:
                ans.append(l)
            r += 1

        return ans
        