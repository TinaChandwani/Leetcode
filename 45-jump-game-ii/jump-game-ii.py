class Solution:
    def jump(self, nums: List[int]) -> int:
        r = 0
        i = 0
        n = len(nums) - 1
        end = 0
        jumps = 0

        while i < n and r < n:
            end = max(end, i + nums[i])
            if i == r:
                jumps += 1
                r = end
            i += 1
        return jumps