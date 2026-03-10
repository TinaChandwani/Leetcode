class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dDict = defaultdict(int)
        active = set()
        l = 0
        r = 0
        n = len(nums)

        while r < n:
            if abs(r-l) <= k:
                if nums[r] not in active:
                    active.add(nums[r])
                else:
                    return True
                r += 1
            else:
                active.remove(nums[l])
                l += 1
        
        return False
