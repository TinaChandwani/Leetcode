class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        '''
        Write Bottom up solution
        [n-forget + 1, n - delay + 1]
        '''
        dp = [-1] * (n+1)
        M = (10**9) + 7
        dp[1] = 1
        for day in range(2,n+1):
            count = 0
            start = max(1, day - forget + 1)
            end = day - delay + 1
            for prev in range(start,end):
                count = (count + dp[prev]) % M 
            dp[day] = count
        start = max(1,n-forget+1)
        end = n + 1
        total = 0
        for d in range(start,end):
            total = (total + dp[d]) % M
        return total