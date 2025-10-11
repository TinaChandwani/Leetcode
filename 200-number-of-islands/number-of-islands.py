class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        q = deque()
        count = 0
        directions = [(0,1), (1,0), (0,-1), (-1,0)]

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    count += 1
                    q.append((i,j))
                    grid[i][j] = '0'
                    while q:
                        r,c = q.popleft()
                        for row,col in directions:
                            nr, nc = row + r, col + c
                            if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == '1':
                                grid[nr][nc] = '0'
                                q.append((nr,nc))
        
        return count