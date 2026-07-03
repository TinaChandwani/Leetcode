class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        res = float('inf')
        diff_arr = [0] * (2*limit + 2)
        m = len(diff_arr)

        for i in range(n//2):
            a = nums[i]
            b = nums[n-1-i]
            s = a + b
            min_s = 1 + min(a,b)
            max_s = limit + max(a,b)
            
            # case0 : zero
            diff_arr[s] -= 1
            diff_arr[s+1] += 1

            # case 1: one
            diff_arr[min_s] -= 1
            diff_arr[max_s + 1] += 1
        
        # prefix sum
        curr = 0

        for k in range(m):
            diff_arr[k] += curr
            curr = diff_arr[k]

            res = min(res, n-(-curr))
        
        
        return res