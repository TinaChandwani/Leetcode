class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n = len(s)
        n1 = len(t)
        if n1 > n:
            return ""
        left = 0
        right = 0
        tDict = defaultdict(int)
        sDict = defaultdict(int)
        l = 0
        r = 0
        counter = 0
        minLength = float("inf")

        for i in t:
            tDict[i] += 1

        while r < n:
            if s[r] in tDict:
                sDict[s[r]] += 1

                if sDict[s[r]] == tDict[s[r]]:
                    counter += 1

            while counter == len(tDict):
                if minLength > r - l + 1:
                    minLength = r - l + 1
                    left = l
                    right = r
                if s[l] in sDict:
                    if sDict[s[l]] == tDict[s[l]]:
                        counter -= 1
                    sDict[s[l]] -= 1
                    if sDict[s[l]] == 0:
                        del sDict[s[l]]
                l += 1

            r += 1

        if minLength == float('inf'):
            return ""
        return s[left : right + 1]
