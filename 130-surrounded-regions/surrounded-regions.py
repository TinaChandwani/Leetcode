class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        q = deque()
        m,n =  len(board),len(board[0])
        visited = [[0 for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    visited[i][j] = 2
                    if i == 0 or i == m-1 or j==0 or j== n-1:
                        visited[i][j] = 1
                        q.append((i,j))
                else:
                    visited[i][j] = 3
        
        while q:
            r,c = q.pop()
            for row,col in [(r,c+1),(r+1,c),(r,c-1),(r-1,c)]:
                if 0<=row<m and 0<=col<n:
                    if visited[row][col] == 2 and board[row][col] == "O" :
                        visited[row][col] = 1
                        q.append((row,col))
        
        for i in range(m):
            for j in range(n):
                if visited[i][j] == 2:
                    board[i][j] = "X"


                

                
        