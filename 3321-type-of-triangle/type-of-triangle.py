class Solution:
    def triangleType(self, nums: List[int]) -> str:
        '''
        Triangle Property : Sum of two sides > third side
        '''
        a,b,c = nums[0],nums[1],nums[2]
        if ((a+b) <= c) or ((b+c) <= a) or ((a + c) <= b):
            return "none"
        elif a == b and a == c:
            return "equilateral"
        elif a != b and a != c and b != c:
            return "scalene"
        else:
            return "isosceles"