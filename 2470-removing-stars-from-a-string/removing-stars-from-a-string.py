class Solution:
    def removeStars(self, s: str) -> str:
        '''
        use Stacks
        '''
        stack = []
        ans = ""
        for i in s:
            if i != '*':
                stack.append(i)
            else:
                if len(s) > 0:
                    stack.pop()
        
        for j in stack:
            ans += j
        
        return ans
        