class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        '''
        DP -> 1) Options to choose right or down; 2) Optimal
        '''
        n = len(grid) # rows
        m = len(grid[0]) # cols
        memo = {}

        def backtrack(r,c):
            if r == n - 1 and c == m - 1:
                return grid[r][c]
            
            if (r,c) in memo:
                return memo[(r,c)]
            
            if r == n - 1:
                # we can only go right
                res = grid[r][c] + backtrack(r, c + 1)
            
            elif c == m - 1:
                res =  grid[r][c] + backtrack(r + 1,c)
            
            else:
                res = grid[r][c] + min(backtrack(r,c+1),backtrack(r+1,c))
            
            memo[(r,c)] = res

            return res
        
        return backtrack(0,0)
