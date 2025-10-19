class NumArray:
    '''
    Follow Up - If I want to get sumRange in O(1) every call
    '''
    def __init__(self, nums: List[int]):
        self.prefix = [0]
        self.prefix_sum = 0
        for i in nums:
            self.prefix_sum += i
            self.prefix.append(self.prefix_sum)

    def sumRange(self, left: int, right: int) -> int:
        if left > right:
            return None

        return self.prefix[right + 1] - self.prefix[left]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)