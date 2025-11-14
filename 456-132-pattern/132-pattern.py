class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        '''
        Plot the numbers in the array as a graph
        '''
        stack = []
        n = len(nums)
        second_max = float('-inf')


        for i in range(n-1,-1,-1):
            # I need to find the second max number
            if nums[i] < second_max:
                return True
            while stack and stack[-1] < nums[i]:
                second_max = stack.pop()
            stack.append(nums[i])
        return False