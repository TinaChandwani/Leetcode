class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        '''
        Constant Space Complexity + Greedy Approach
        The first picked element is always index 0 (even -> +)
        second picked element is index 1 (odd -> -)
        3 choices
        1) skip
        2) take it as +
        3) take it as -
        but for 2 and 3 the rule is:
            1) we can only take + if previous was -
            2) we can only take - if previous was +
        The ans will be even because alternating sum will always start with +
        '''
        even, odd = 0,0
        for i in nums:
            new_even = max(even,odd + i)
            new_odd = max(odd, even - i)
            even,odd = new_even,new_odd
        return even
