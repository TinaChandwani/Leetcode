class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        '''
        Approach 1: Using stacks
        '''
        stack = []
        remove = set()
        ans = ''
        
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            elif s[i] == ')':
                if len(stack) > 0:
                    stack.pop()
                else:
                    remove.add(i)
        
        while len(stack) > 0:
            remove.add(stack.pop())
        
        for k in range(len(s)):
            if k in remove:
                continue
            else:
                ans += s[k]
        
        return ans