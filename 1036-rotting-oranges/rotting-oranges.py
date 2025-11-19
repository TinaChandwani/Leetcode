class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        '''
        Basically need BFS
        '''
        q = deque()
        rotten = 2
        fresh = 1
        tfresh = 0
        tmins = -1
        m = len(grid) # rows
        n = len(grid[0]) # cols
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        visit = set()
        # Add all the rotten oranges into queue

        for i in range(m):
            for j in range(n):
                if grid[i][j] == rotten:
                    q.append((i,j))
                if grid[i][j] == fresh:
                    tfresh += 1
        
        if tfresh == 0: 
            # Basically all rotten in the grid just return
            return 0
        
        while q:
            l = len(q)
            for i in range(l):
                r,c = q.popleft()
                for row,col in directions:
                    nr = r + row
                    nc = c + col
                    if 0 <= nr < m and 0 <= nc < n and (nr,nc) not in visit and grid[nr][nc] == fresh:
                        q.append((nr,nc))
                        visit.add((nr,nc))
                        tfresh -= 1
            tmins += 1
        
        if tfresh == 0:
            return tmins
        else:
            return -1

