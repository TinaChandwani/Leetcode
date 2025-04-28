class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        q1 = deque()
        q2 = deque()
        m,n = len(heights), len(heights[0])
        visited = [[0 for _ in range(n) ]for __ in range(m)]
        visited2 = [[0 for at in range(n)] for la in range(m)]
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        set1 = []
        set2 = []
        output = []

        # First let's tackle Pacific ocean
        for i in range(m):
            for j in range(n):
                if i == 0:
                    visited[i][j] = 1
                    set1.append([i,j])
                if j == 0:
                    visited[i][j] = 1
                    set1.append([i,j])
        
        for (p,a) in set1:
            q1.append((p,a))

        while q1:
            row, col = q1.popleft()
            for dx, dy in directions:
                new_x, new_y = row + dx, col + dy
                if 0 <= new_x < m and 0 <= new_y < n and visited[new_x][new_y] == 0 and heights[new_x][new_y] >= heights[row][col] :
                    visited[new_x][new_y] = 1
                    q1.append((new_x,new_y))
                    set1.append([new_x,new_y])
        
        # Similarily we will tackle Atlantic Ocean

        for o in range(m):
            for k in range(n):
                if o == m-1:
                    visited2[o][k] = 1
                    set2.append([o,k])
                if k == n - 1:
                    visited2[o][k] = 1
                    set2.append([o,k])
        
        for a,t in set2:
            q2.append((a,t))
        
        while q2:
            row,col =  q2.popleft()
            for dx,dy in directions:
                new_x,new_y = row + dx, col + dy
                if 0 <= new_x < m and 0 <= new_y < n and visited2[new_x][new_y] == 0 and heights[new_x][new_y] >= heights[row][col]:
                    visited2[new_x][new_y] = 1
                    q2.append((new_x,new_y))
                    set2.append([new_x,new_y]) 


        # Now the Ans
        for i in range(m):
            for j in range(n):
                if visited[i][j] and visited2[i][j]:
                    output.append([i,j])

        return output      

            