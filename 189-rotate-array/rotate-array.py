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
        k = k % n
        if k != 0:
            nums[:k],nums[k:] = nums[-k:],nums[:-k]
        
        