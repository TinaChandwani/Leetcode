class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        '''
        Pairs always start at even indices.
        Jaha khade ho -> right side mein kitne elements hain
        if (i+1) == khada hu :
            Yes:
                odd : single element
                even : nahi hoga waha single element
        elif (i+1) != khande hu:
            even : left mein hoga single element
            odd : right side mein hi pakka single element hain
        '''

        l = 0
        r = len(nums) - 1

        while l < r:
            m = l + (r-l) // 2
            if m % 2 == 1:
                m -= 1 # Pairs always start at even indices.
            
            if nums[m] == nums[m+1]:
                l = m + 2
            else:
                r = m
        
        return nums[l]
 