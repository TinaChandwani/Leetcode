class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        n = len(grid) # rows
        m = len(grid[0])
        memo = {}

        def backtrack(r,c,product):
            if r == n - 1 and c == m - 1:
                return product
            
            if (r,c,product) in memo:
                return memo[(r,c,product)]
            
            direction = [(0,1),(1,0)]
            best = float("-inf")

            for i, j in direction:
                new_r = r + i
                new_c = c + j
                if 0 <= new_r < n and 0 <= new_c < m:
                    new_product = product * (grid[new_r][new_c])
                    best = max(best,backtrack(new_r,new_c,new_product))
            memo[r,c,product] = best
            
            return best
        
        ans = backtrack(0,0,grid[0][0])

        if ans < 0:
            return -1
        return ans % (10**9 + 7)
