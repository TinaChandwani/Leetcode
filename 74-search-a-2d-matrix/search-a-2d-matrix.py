class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        '''
        Basically I will compare the target with every row first element
        if whichever first row it comes then apply Binary search only for that 
        row -> This is wrong because the complexity for this is O(m*logn)
        Second Approach :-
        1. Flatten the 2D array into 1D -> O(1) time because we just use index math and don't copy anything
        2. Apply Binary search on that -> log(m*n) -> m*n is the size of the flattened array

        To Flatten 2D array into 1D :-
        row = k / n
        col = k mod n
        where n = number of columns in matrix
        k = index of 1D array
        1D index (k) = row * n + col
        '''
        if not matrix or not matrix[0]:
            return False
        def bs(l,r,arr):
            while r >= l:
                m = (l + r) // 2
                if arr[m] == target:
                    return True
                elif arr[m] < target:
                    l = m + 1
                else:
                    r = m - 1
            return False
        
        m = len(matrix) #rows
        n = len(matrix[0]) #cols
        total = n * m
        arr = []
        for i in range(total):
            row = i // n
            col = i % n
            ele = matrix[row][col]
            arr.append(ele)
        
        return bs(0,total-1,arr)


