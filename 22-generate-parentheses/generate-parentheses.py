class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        def backtrack(current,openc,close):
            if openc == n and close == n:
                result.append(current)
                return
            
            if openc < n:
                backtrack(current + "(",openc + 1, close)
            
            if close < openc:
                backtrack(current + ")",openc,close + 1)
        
        backtrack("",0,0)
        return result