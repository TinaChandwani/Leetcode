class Solution:
    def checkValidString(self, s: str) -> bool: 
        stack = [] # (index)
        star = [] # (index)
        n = len(s)

        for i in range(n):
            if s[i] == '(':
                stack.append(i)
            elif s[i] == '*':
                star.append(i)
            else:
                if len(stack) <= 0 and len(star) <= 0:
                    return False
                else:
                    if len(stack) > 0:
                        stack.pop()
                    elif len(star) > 0:
                        star.pop()
        
        while len(stack) > 0 and len(star) > 0:
            index = stack.pop()
            index2 = star.pop()
            if index2 < index:
                return False
        
        return len(stack) == 0


        
        