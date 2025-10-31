class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        '''
        Time Complexity :- O(mn) and Space Complexity -> O(m+n)
        '''

        zrows = set()
        zcols = set()
        m = len(matrix) # rows
        n = len(matrix[0]) # cols

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    zrows.add(i)
                    zcols.add(j)
        print(f'zcols {zcols} and zrows {zrows}')
        if len(zcols) == 0 and len(zrows) == 0:
            return matrix
        
        for k in range(m):
            for l in range(n):
                if k in zrows or l in zcols:
                    matrix[k][l] = 0