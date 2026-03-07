class Solution:
    def checkValidString(self, s: str) -> bool:
        o,c = 0,0
        for i in s:
            if i == "*" or i == '(':
                o += 1
            else:
                if o > 0:
                    o -= 1
                else:
                    return False
        
        for j in range(len(s)-1,-1,-1):
            if s[j] == '*' or s[j] == ')':
                c += 1
            else:
                if c > 0:
                    c -= 1
                else:
                    return False
        
        return True
        