class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board) # rows
        n = len(board[0]) # cols
        q = deque()
        visited = [[0 for _ in range(n)] for j in range(m)]
        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O' and (i == 0 or j == 0 or i == m-1 or j == n-1):
                    q.append((i,j))
                    visited[i][j] = 1
 
        
        while q:
            r,c = q.popleft()
            for row,col in directions:
                nr = row + r
                nc = col + c
                if 0 <= nr < m and 0 <= nc < n and board[nr][nc] == 'O' and visited[nr][nc] == 0:
                    visited[nr][nc] = 1
                    q.append((nr,nc))
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O' and visited[i][j] == 0:
                    board[i][j] = 'X'
      