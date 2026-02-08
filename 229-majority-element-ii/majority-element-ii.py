class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        first, second = None, None
        ans = []
        count1,count2 = 0,0
        for i in nums:
            if i == first:
                count1 += 1
            elif i == second:
                count2 += 1
            elif count1 == 0:
                first = i
                count1 = 1
            elif count2 == 0:
                second = i
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1
        
        c1 ,c2 = 0,0
        for j in nums:
            if j == first:
                c1 += 1
            if j == second:
                c2 += 1
        
        n = len(nums)
        maj = int(n // 3)
        if c1 > maj:
            ans.append(first)
        if second != first and c2 > maj:
            ans.append(second)
        
        return ans

        