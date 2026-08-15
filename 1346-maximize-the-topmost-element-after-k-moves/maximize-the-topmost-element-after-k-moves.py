class Solution:
    def maximumTop(self, nums: List[int], k: int) -> int:
        if k == 0:
            return nums[0]
        
        if len(nums) == 1:
            if k % 2 == 0:
                return nums[0]
            else:
                return -1
        
    
        maxT = -1
        i = 0

        while i < len(nums) and k > 1:
            maxT = max(maxT, nums[i])
            k -= 1
            i += 1

        if k == 1:
            if i + 1 < len(nums):
                return max(maxT,nums[i + 1])

        return maxT
