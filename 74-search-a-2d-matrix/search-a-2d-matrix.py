class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        '''
        Basically the approach is :
        1. Do a binary search for the rows
        2. Do a binary search in that row
        '''
        if not matrix or not matrix[0]:
            return False
        n = len(matrix) # rows
        m = len(matrix[0]) #cols
        gl = 0
        gr = n - 1
        res_row = -1
        def bs(l,r,row):
            while r >= l:
                m = (l + r) // 2
                if target == matrix[row][m]:
                    return True
                elif target < matrix[row][m]:
                    r = m - 1
                else:
                    l = m + 1
            return False
            
        while gr >= gl:
            mr = (gl + gr) // 2
            if matrix[mr][0] <= target <= matrix[mr][m-1]:
                res_row = mr
                break
            elif matrix[mr][0] < target:
                gl = mr + 1
            else:
                gr = mr - 1
        
        return res_row!=-1 and bs(0,m-1,res_row)

       