class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        store_k = k
        j = n - 1
        i = 0 
        while i < j:
            nums[i],nums[j] = nums[j],nums[i]
            j = j - 1
            i = i + 1

        # Reverse in the array
        left = 0
        right  = store_k - 1


        while left < right:
            nums[left],nums[right] = nums[right],nums[left]
            right = right - 1
            left = left + 1
        
        left = store_k
        right = n - 1
        
        while left < right:
            nums[left],nums[right] = nums[right],nums[left]
            right = right - 1
            left = left + 1
        