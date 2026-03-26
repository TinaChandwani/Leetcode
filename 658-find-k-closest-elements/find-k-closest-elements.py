class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        '''
        If k == arr.length => entire array would be the ans
        '''
        if k == len(arr):
            return arr

        ans = []
        l = 0
        r = len(arr) - 1

        while l < r:   
            m = (l+r) // 2
            if arr[m] >= x:
                r = m
            else:
                l = m + 1
        
        i = 0
        l = r - 1
        
        while i < k:
            if l == -1:
                r = r + 1
            elif r == len(arr):
                l = l - 1
            elif abs(arr[l] - x) <= abs(arr[r] - x):
                l -= 1
            else:
                r += 1
            i += 1
        
        return arr[l+1:r]
