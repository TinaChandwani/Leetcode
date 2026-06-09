class Solution:

    def __init__(self, nums: List[int]):
        self.arr = nums.copy()

    def reset(self) -> List[int]:
        return self.arr.copy()
        

    def shuffle(self) -> List[int]:
        nums = self.arr.copy() 
        temp = []
        for i in range(len(nums)):
            num = random.choice(nums)
            temp.append(num)
            nums.remove(num)
        
        return temp


        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()