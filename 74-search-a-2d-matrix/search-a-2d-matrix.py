class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        m = len(matrix) #rows
        n = len(matrix[0]) # cols
        total = m * n
        l = 0
        r = total - 1
        while r >= l:
            m = (l+r)//2
            row = m // n
            col = m % n
            val = matrix[row][col]
            if val == target:
                return True
            elif target < val:
                r = m - 1
            else:
                l = m + 1
        return False
        