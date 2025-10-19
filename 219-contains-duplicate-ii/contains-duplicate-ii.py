class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k <= 0:
            return False
        n = len(nums)
        last = {}
        i = 0
        while i < n:
            x = nums[i]
            if x in last:
                limit = last[x]
                if abs(i - limit) <= k and nums[i] == nums[limit]:
                    return True
            last[x] = i 
            i += 1
        return False
