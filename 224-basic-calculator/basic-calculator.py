class Solution:
    def calculate(self, s: str) -> int:
        '''
        First writing code without Parenthesis to build the.
        For Parenthesis we need stack to store the sign and total before every (
        in the stack 
        '''
        total = 0
        current = 0
        i = 0
        sign = 1
        n = len(s)
        stack = []

        while i < n:
            ch = s[i]
            # Space
            if ch == ' ':
                i += 1
                continue
            # Number
            if ch.isdigit():
                current = current * 10 + int(ch)
            
            elif ch == "+" or ch == '-':
                total += sign * current
                current = 0
            
                if ch == '+':
                    sign = 1
                else:
                    sign = -1
            elif ch == '(':
                stack.append(total)
                stack.append(sign)
                total = 0
                sign = 1
                current = 0
            elif ch == ')':
                total += sign * current
                current = 0
                prev_sign = stack.pop()
                prev_total = stack.pop()
                total = prev_total + prev_sign * total
            i += 1
        total += sign * current
        return total
            

