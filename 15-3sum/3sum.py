class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        n = len(nums) - 2

        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j = i + 1
            k = len(nums) - 1
            while j < k:
                target = nums[i] + nums[j] + nums[k]
                if target == 0 :
                    ans.append([nums[i],nums[j],nums[k]])
                    j += 1
                    k -= 1
                    while j < k and nums[j-1] == nums[j]:
                        j += 1
                elif target > 0:
                    k -= 1
                elif target < 0:
                    j += 1
        return ans