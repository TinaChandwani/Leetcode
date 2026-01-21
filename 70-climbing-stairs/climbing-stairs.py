class Solution:
    def climbStairs(self, n: int) -> int:
        '''
        This is similar to Fibonacci series.
        i ka nikalne ke lie, you just need 1 pehle and 2 pehle
        '''
        if n <= 2:
            return n
        a,b = 1,2
        for i in range(3,n+1):
            a,b = b,a+b
        return b