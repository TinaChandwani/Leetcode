class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        min_position = -1
        max_position = -1
        cult_ind = -1
        ans = 0

        for i in range(len(nums)):
            if nums[i] == minK:
                min_position = i
            if nums[i] == maxK:
                max_position = i
            if nums[i] > maxK or nums[i] < minK:
                cult_ind = i
            
            smaller = min(min_position,max_position)
            temp = smaller - cult_ind
            if temp >= 0:
                ans += temp

        return ans
                
        