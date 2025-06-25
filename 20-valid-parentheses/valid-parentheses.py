class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matching = {')':'(','}':'{',']':'['}
        for i in s:
            if i in matching.values():
                stack.append(i)
            else:
                if not stack:
                    return False
                elif matching[i] == stack[-1]:
                    stack.pop()
                else:
                    return False
        return not stack