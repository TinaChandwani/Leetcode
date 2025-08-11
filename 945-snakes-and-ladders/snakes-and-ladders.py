class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        # BFS Technique
        length = len(board)
        board.reverse()

        def cal_row_col(s):
            row = (s-1) // length
            col = (s-1) % length
            if row % 2 == 1:
                col = length - 1 - col
            return [row,col]
        
        # BFS Implementation
        q = deque()
        visit = set()
        q.append([1,0]) # [squares,moves]

        while q:
            s, m = q.popleft()
            for i in range(1,7):
                next_s = s + i
                if next_s > length * length: 
                    continue
                r,c = cal_row_col(next_s)
                if board[r][c] != -1:
                    next_s = board[r][c]
                if next_s == (length * length):
                    return m + 1
                if next_s not in visit:
                    visit.add(next_s)
                    q.append([next_s,m+1])
        
        return -1