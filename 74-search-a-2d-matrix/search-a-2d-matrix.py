class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        def row_find(l,r):
            while l <= r:
                m = l + (r-l) // 2
                if matrix[m][0] == target:
                    return m
                elif matrix[m][0] < target:
                    l = m + 1
                else:
                    r = m - 1
            return r
        
        row = row_find(0,len(matrix) - 1)
        col = len(matrix[0])

        if row < 0:
            return False
        # l = matrix[row][0]
        # r = matrix[row][col]
        left = 0
        right = col - 1

        while left <= right:
            m = left + (right - left) // 2
            if matrix[row][m] == target:
                return True
            elif matrix[row][m] < target:
                left = m + 1
            else:
                right = m - 1
        
        return False