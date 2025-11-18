from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        '''
        Time Complexity : O(m * n) -> the two for loops visits every cell once
        Space Complexity : O(m * n) -> the whole grid is land
        '''
        
        m = len(grid) # rows
        n = len(grid[0]) # cols
        visit = set()
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        max_count = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 :
                    q = deque()
                    q.append((i,j))
                    count = 1
                    while q:
                        r,c = q.popleft()
                        visit.add((r,c))
                        for row,col in directions:
                            nr = r + row
                            nc = c + col
                            if 0 <= nr < m and 0 <= nc < n and (nr,nc) not in visit and grid[nr][nc] == 1:
                                q.append((nr,nc))
                                visit.add((nr,nc))
                                count += 1
                    max_count = max(max_count,count)
        
        return max_count
                                
                            

