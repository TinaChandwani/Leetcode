class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        def solve(s,p):
            # Base Case -> if both s and p goes out of bounds
            if len(p) == 0:
                if len(s) == 0:
                    return True
                return False
            
            if len(s) > 0 and (p[0] == s[0] or p[0] == '.'):
                isMatched = True
            else:
                isMatched = False
            
            dont_take = False
            take = False
            check = False
            
            if len(p) > 1 and p[1] == '*':
                # Don't take
                if solve(s,p[2:]):
                    dont_take = True

                # Take
                if isMatched and solve(s[1:],p):
                    take = True

            else:
                # check characters
                if isMatched and solve(s[1:],p[1:]):
                    check = True

            
            return dont_take or take or check

        return solve(s,p)