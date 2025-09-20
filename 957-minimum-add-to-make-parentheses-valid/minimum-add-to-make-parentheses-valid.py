class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        ob = 0
        cb = 0
        ans = 0

        for i in s:
            if i == '(':
                stack.append(i)
                ob += 1
            else:
                cb += 1
                if not stack and cb != 0:
                    ans += 1
                else: 
                    stack.pop()
        if stack:
            n = len(stack)
            ans += n
        return ans

