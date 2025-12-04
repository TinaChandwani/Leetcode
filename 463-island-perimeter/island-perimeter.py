class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        '''
        Basically do BFS /DFS and check neighbours, if they are 1 then continue else add in perimeter
        '''
        q = deque()
        m = len(grid)
        n = len(grid[0])
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        ans = 0
        found = False
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    q.append((i,j))
                    grid[i][j] = -1
                    found = True
                    break
            if found:
                break
        while q:
            r,c  = q.popleft()
            for row,col in directions:
                nr,nc = row + r , col + c
                if not (0 <= nr < m and 0 <= nc < n):
                    ans += 1
                    continue
                if grid[nr][nc] == 0:
                    ans += 1
                    continue
                if grid[nr][nc] == 1:
                    q.append((nr,nc))
                    grid[nr][nc] = -1
        return ans
                
