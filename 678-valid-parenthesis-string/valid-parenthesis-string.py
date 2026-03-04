class Solution:
    def checkValidString(self, s: str) -> bool:
        '''
        Since * -> has multiple options
        Whenever we have options -> Try Recursion + memoization.
        It has multiple approaches but the ideal is DP
        '''
        if s[0] == ')':
            return False
        memo = {}
        
        def solve(i,open_count):
            if open_count < 0:
                return False

            if i == len(s):
                return open_count == 0

            if (i,open_count) in memo:
                return memo[(i,open_count)]


            if s[i] == '(':
                isValid = solve(i + 1,open_count + 1) 
            elif s[i] == '*':
                isValid = (solve(i + 1,open_count + 1) or solve(i + 1,open_count - 1) or
                            solve(i + 1,open_count) ) 
            else:
                isValid = solve(i + 1,open_count - 1)
            
            memo[(i,open_count)] = isValid
            return isValid
        
        return solve(0,0)

        