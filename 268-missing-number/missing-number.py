class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        total = sum(nums)
        miss_total = n * (n+1) // 2
        miss_no = miss_total - total
        return miss_no