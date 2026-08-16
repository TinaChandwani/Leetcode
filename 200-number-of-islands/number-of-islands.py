from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        q = deque()
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        island = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    q.append((i,j))
                    while q :
                        i1,j1 = q.pop()
                        grid[i1][j1] = "0"

                        for r,c in directions:
                            new_r = i1 + r
                            new_c = j1 + c
                            if 0 <= new_r < m and 0 <= new_c < n and grid[new_r][new_c] == "1":
                                q.append((new_r,new_c))

                    island += 1
        
        return island