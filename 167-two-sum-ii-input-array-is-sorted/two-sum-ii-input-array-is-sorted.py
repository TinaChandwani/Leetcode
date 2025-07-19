class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 2:
            return [1,2]
        i = 0
        j = len(nums) - 1
        
        while i < j:
            k = nums[i] + nums[j]
            if k == target:
                return [i+1, j+1]
            elif k > target:
                j -= 1
            else:
                i += 1
            
