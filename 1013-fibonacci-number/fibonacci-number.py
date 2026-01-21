class Solution:
    def fib(self, n: int) -> int:
        '''
        Constant Space Complexity
        '''
        if n <= 1:
            return n
        a = 0
        b = 1
        for i in range(1,n):
            a,b = b,a+b
        return b
        