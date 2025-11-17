class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        token = ('+','-','*','/')
        n = len(tokens)
        for i in range(n):
            if tokens[i] not in token:
                stack.append(tokens[i])
            else:
                a = int(stack.pop())
                b = int(stack.pop())
                if tokens[i] == '+':
                    c = a + b
                elif tokens[i] == '-':
                    c = b - a
                elif tokens[i] == '*':
                    c = a * b
                else:
                    c = b / a
                stack.append(c)
        return int(stack[-1])
            
