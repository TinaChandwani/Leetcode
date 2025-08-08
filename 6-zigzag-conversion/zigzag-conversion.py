class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        matrix = [[] for i in range(numRows)]
        d = 1
        i = 0
        ret = ''
        
        for char in s:
            matrix[i].append(char)
            if i == 0:
                d = 1
            elif i == numRows - 1:
                d = -1
            i += d
        
        for j in range(numRows):
            ret += ''.join(matrix[j])
        
        return ret