class NumArray:

    def __init__(self, nums: List[int]):
        self.ans = 0
        self.nums = nums
        

    def sumRange(self, left: int, right: int) -> int:
        if right < left:
            return None
        self.ans = 0
        while left <= right:
            self.ans += self.nums[left]
            left += 1
        return self.ans

        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)