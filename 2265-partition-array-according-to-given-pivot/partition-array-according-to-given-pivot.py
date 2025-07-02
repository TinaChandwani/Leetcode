class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less, equal , big = [],[],[]

        for num in nums:
            if num < pivot:
                less.append(num)
            elif num == pivot:
                equal.append(num)
            else:
                big.append(num)
        
        return less + equal + big