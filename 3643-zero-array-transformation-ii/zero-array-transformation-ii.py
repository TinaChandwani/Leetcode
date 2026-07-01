class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        diff = [0] * n
        t = 0          
        l = 0
        r = len(queries)

        def checkDiffArr(idx):
            diff_arr = [0] * (n + 1)

            for i in range(idx):
                start,end,val = queries[i]
                diff_arr[start] += val
                if end + 1 < n:
                    diff_arr[end + 1] -= val
            
            # prefix sum
            for i in range(1,n):
                diff_arr[i] += diff_arr[i-1]
  
            for i in range(n):
                if diff_arr[i] < nums[i]:
                    return False
            
            return True
        
        if checkDiffArr(0):
            return 0
        
        if not checkDiffArr(len(queries)):
            return -1

        while l < r:
            mid = (l + r) // 2
            if checkDiffArr(mid):
                r = mid
            else:
                l = mid + 1

        return l