class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index = {}

        for i in range(len(nums)):
            dest = target - nums[i]
            if dest in index:
                return [index[dest],i]
            else:
                index[nums[i]] = i
        