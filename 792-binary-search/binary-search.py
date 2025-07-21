class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0 :
            return -1
        left = 0
        right = len(nums) - 1

        def helper(left,right,nums):
            if left > right:
                return -1
            middle = (right + left) // 2

            if nums[middle] == target:
                return middle
            
            if nums[middle] > target:
                return helper(left,middle - 1,nums)
            else:
                return helper(middle + 1,right,nums)
            
        
        ans = helper(left,right,nums)
        return ans
