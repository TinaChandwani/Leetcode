class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowsDict = {}
        colsDict = {}
        boxesDict = {}

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                if i in rowsDict:
                    if board[i][j] in rowsDict[i]:
                        return False
                    else:
                        rowsDict[i].add(board[i][j])
                else:
                    rowsDict[i] = {board[i][j]}
                
                if j in colsDict:
                    if board[i][j] in colsDict[j]:
                        return False
                    else:
                        colsDict[j].add(board[i][j])
                else:
                    colsDict[j] = {board[i][j]}
                
                boxi = i // 3
                boxj = j // 3

                if (boxi,boxj) not in boxesDict:
                    boxesDict[(boxi, boxj)] = set()

                if board[i][j] in boxesDict[(boxi,boxj)]:
                    return False
                else:
                    boxesDict[(boxi,boxj)].add(board[i][j])
        
        return True