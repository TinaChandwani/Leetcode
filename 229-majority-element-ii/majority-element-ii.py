class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        '''
        we need n / 3 times -> atmost 2 elements
        '''
        candidate1 = None
        candidate2 = None
        c1 = 0
        c2 = 0
        maj = len(nums) / 3
        ans = []

        for num in nums:
            if num == candidate1:
                c1 += 1
            elif num == candidate2:
                c2 += 1
            elif c1 == 0:
                candidate1 = num
                c1 = 1
            elif c2 == 0:
                candidate2 = num
                c2 = 1
            else:
                c1 -= 1
                c2 -= 1
        
        # pass 2 : verify (since we need atmost 2)

        c1 = 0
        c2 = 0

        for num in nums:
            if num == candidate1:
                c1 += 1
            elif num == candidate2:
                c2 += 1
        
        if c1 > maj:
            ans.append(candidate1)
        
        if c2 > maj:
            ans.append(candidate2)
        
        return ans