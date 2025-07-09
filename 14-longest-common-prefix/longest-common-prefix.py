class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        ans = ""
        for i in range(len(strs[0])):
            char = strs[0][i]
            for j in strs[1:]:
                if i >= len(j) or j[i] != char:
                    return ans
            ans += char
        return ans