class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        n = len(nums)
        l = 0
        r = 0
        count = 0
        mpp = defaultdict(int)
        prefix_l = 0

        while r < n:
            mpp[nums[r]] += 1
            while len(mpp) > k:
                prefix_l = 0
                mpp[nums[l]] -= 1
                if mpp[nums[l]] == 0:
                    del mpp[nums[l]]
                l = l + 1
            while mpp[nums[l]] > 1 and len(mpp) == k:
                mpp[nums[l]] -= 1
                l = l + 1
                prefix_l = prefix_l + 1
            
            if len(mpp) == k:
                count += 1 + prefix_l 
            
            r += 1
        
        return count