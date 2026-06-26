class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n = len(nums) - 1
        count = 0

        for i in range(n + 1):
            # check if the number is +ve or -ve
            num = abs(nums[i])

            if num > n:
                return False

            if num == n:
                count += 1
            
            if count > 2:
                return False
            
            if num != n and nums[num-1] < 0:
                return False
            
            if (num != n) or (num == n and count <= 1):
                nums[num - 1] = nums[num - 1] * -1
        
        
        if count < 2:
            return False

        for i in range(n):
            if nums[i] > 0:
                return False
        
        return True