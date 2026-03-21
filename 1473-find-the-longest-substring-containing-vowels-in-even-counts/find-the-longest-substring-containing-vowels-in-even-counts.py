class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        vDict = {}
        vDict['00000'] = -1
        result = 0
        vowels = [0] * 5 #[a,e,i,o,u]

        for i in range(len(s)):
            if s[i] == 'a':
                vowels[0] = (vowels[0] + 1) % 2
            elif s[i] == 'e':
                vowels[1] = (vowels[1] + 1) % 2
            elif s[i] == 'i':
                vowels[2] = (vowels[2] + 1) % 2
            elif s[i] == 'o':
                vowels[3] = (vowels[3] + 1) % 2
            elif s[i] == 'u':
                vowels[4] = (vowels[4] + 1) % 2
            
            v = ''.join(map(str,vowels))
            if v in vDict:
                result = max(result,i - vDict[v])
            else:
                vDict[v] = i

        return result