class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        setNums = set(nums)
        n = len(setNums)
        longest = 0

        for i in setNums:
            currLength = 1
            if i-1 not in setNums:
                while i+1 in setNums:
                    currLength += 1
                    i = i + 1
                longest = max(longest,currLength)
        return longest
