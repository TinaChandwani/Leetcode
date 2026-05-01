class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        '''
        Classic Backtracking
        '''
        m = len(grid) #rows
        n = len(grid[0]) #cols
        start = (0,0)
        end = (0,0)
        count_of_zero = 0

        def backtrack(x,y,c):
            if grid[x][y] == -1:
                return 
            if grid[x][y] == 2:
                if c == count_of_zero + 1:
                    return 1
                else:
                    return 0

            directions = [(1,0),(0,1),(-1,0),(0,-1)]
            temp = grid[x][y]
            grid[x][y] = -1
            paths = 0

            for i,j in directions:
                x_new = x + i
                y_new = y + j
                if 0 <= x_new < m and 0 <= y_new < n and grid[x_new][y_new] != -1:
                    paths += backtrack(x_new,y_new,c+1)
            
            grid[x][y] = temp
            return paths

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    start = (i,j)
                elif grid[i][j] == 2:
                    end = (i,j)
                elif grid[i][j] == 0:
                    count_of_zero += 1
        
        return backtrack(start[0],start[1],0)
