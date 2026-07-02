class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n = len(nums)
        m = len(queries)

        diff_arr = [0] * (n + 1)

        for start, end in queries:
            diff_arr[start] += 1
            if end + 1 < n:
                diff_arr[end + 1] -= 1
        
        curr = 0
        for i in range(n):
            diff_arr[i] += curr
            curr = diff_arr[i]
            if diff_arr[i] < nums[i]:
                return False
        
        return True
        