class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
        m = len(matrix)
        n = len(matrix[0])
        top = 0
        bottom = m - 1
        left = 0
        right = n - 1
        ans = []

        while top <= bottom and left <= right:
            for i in range(left,right+1):
                ans.append(matrix[top][i])
            for j in range(top+1,bottom+1):
                ans.append(matrix[j][right])
            if top < bottom:
                for k in range(right-1,left-1,-1):
                    ans.append(matrix[bottom][k])
            if left < right:
                for l in range(bottom-1,top,-1):
                    ans.append(matrix[l][left])
            top += 1
            bottom -= 1
            left += 1
            right -= 1
        
        return ans