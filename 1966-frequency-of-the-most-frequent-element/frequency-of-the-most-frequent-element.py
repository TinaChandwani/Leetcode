class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        l = 0
        r = 1
        cost = 0
        ans = 1

        while r < len(nums):
            diff = nums[r] - nums[r-1]
            cost += diff * (r - l)

            while cost > k:
                cost -= nums[r] - nums[l]
                l += 1
            
            ans = max(ans,r-l+1)
            r += 1
        
        return ans