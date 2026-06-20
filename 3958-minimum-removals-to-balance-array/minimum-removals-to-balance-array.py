class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        i = 0
        j = 0
        longest = 0

        for j in range(n):
            while nums[j] > nums[i] * k:
                i += 1 
            
            longest = max(longest,j - i + 1)
        
        return (n - longest)