class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hashMap = {}

        for i in range(len(s)):
            if s[i] not in hashMap:
                if t[i] in hashMap.values():
                    return False
                else:
                    hashMap[s[i]] = t[i]
            else:
                if hashMap[s[i]] != t[i]:
                    return False
                else:
                    continue
        return True