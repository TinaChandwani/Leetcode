class Solution:
    def maxDepth(self, s: str) -> int:
        stack = 0
        ans = 0


        for i in s:
            ans = max(ans,stack)
            if i == '(':
                stack += 1
            elif i == ')':
                stack -= 1
        return ans

        