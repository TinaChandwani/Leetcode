class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        charMap = {}
        n = len(s)

        for i in range(n):
            if s[i] in charMap:
                if charMap[s[i]] != t[i]:
                    return False
            elif t[i] in charMap.values():
                return False
            charMap[s[i]] = t[i]
        return True
            