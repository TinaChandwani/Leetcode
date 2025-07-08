class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        '''
        Basically the Algorithm is 
        1) First Reverse the entire Array
        2) reverse from 0 -> ((k%n) -1 )
        3) reverse from (k%n) -> end of array
        '''
        n = len(nums)
        rotateTimes = k % n
        # Reversing the entire array
        i = 0
        j = n - 1
        while i < j:
            nums[i],nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
        
        # Reverse the First Part
        i = 0
        j = rotateTimes - 1

        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
        
        # Reverse the Second Part
        i = rotateTimes
        j = n - 1

        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
        