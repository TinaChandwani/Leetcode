class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        res = 0
        maxJ = 0
        currentend = 0
        last = len(nums) - 1

        for i in range(len(nums)):
            max_jumps = nums[i] + i
            maxJ = max(maxJ,max_jumps)

            if i == currentend:
                res += 1
                currentend = maxJ

            if currentend >= last:
                break

        return res