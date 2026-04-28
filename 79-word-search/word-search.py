class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        '''
        Classic Backtracking problem:
        '''
        m = len(board) # rows
        n = len(board[0]) # cols

        def solve(i,j,idx):
            if idx == len(word):
                return True

            if i < 0 or j < 0 or i >= m or j >= n or board[i][j] == '$':
                return False
            
            if board[i][j] != word[idx]:
                return False
            
            temp = board[i][j]
            board[i][j] = '$'
            directions = [(1,0),(0,1),(-1,0),(0,-1)]
            for r,c in directions:
                new_i = i + r
                new_j = j + c
                if solve(new_i,new_j,idx+1):
                    return True
            
            board[i][j] = temp
            return False
        
       
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0] and solve(i,j,0):
                    return True
        
        return False
