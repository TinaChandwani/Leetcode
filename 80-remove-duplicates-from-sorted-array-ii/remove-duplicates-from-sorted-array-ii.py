class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        j = 1
        k = 1
        lc = 1

        while j < len(nums):
            if nums[i] != nums[j]:
                i = i + 1
                j = j + 1
                k = k + 1
                lc = 1
            else:
                lc = lc + 1
                if lc > 2:
                    nums.pop(j)
                    lc = lc - 1  
                else:
                    i = i + 1
                    j = j + 1
                    k = k + 1
        return k


        