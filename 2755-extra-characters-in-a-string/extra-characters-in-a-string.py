class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        '''
        Every index i has two choices :
            -> Not taking s[i] as extra character
            -> 1 + Taking s[i] as extra character
        
        recursion
        '''
        dSet = set(dictionary)
        n = len(s)
        memo = {}
        def solve(i):
            if i >= n:
                return 0

            if i in memo:
                return memo[i]

            # not taking    
            res = 1 + solve(i+1)

            for j in range(i,n):
                curr = s[i:j+1]
                if curr in dSet:
                    res = min(res,solve(j+1))
            
            memo[i] = res
            
            return res
            
        
        return solve(0)