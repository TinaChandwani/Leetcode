class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            num = abs(nums[i])
            idx = num - 1
            if nums[idx] < 0:
                return num
            else:
                nums[idx] = nums[idx] * -1
        