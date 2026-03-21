class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        vDict = {}
        vDict[0] = -1
        result = 0
        mask = 0

        for i in range(len(s)):
            if s[i] == 'a':
                mask = mask ^(1 << 0)
            elif s[i] == 'e':
                mask = mask ^(1 << 1)
            elif s[i] == 'i':
                mask = mask ^(1 << 2)
            elif s[i] == 'o':
                mask = mask ^(1 << 3)
            elif s[i] == 'u':
                mask = mask ^(1 << 4)
            
            if mask in vDict:
                result = max(result,i - vDict[mask])
            else:
                vDict[mask] = i

        return result