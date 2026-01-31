class Solution:
    def solve(self,day,memo,forget,delay):
        # Returns no of people knows the secret till day n
        if day == 1:
            return 1
        if day in memo:
            return memo[day]
        result = 0
        start = max(1, day - forget + 1)
        end = day - delay + 1
        for i in range(start,end):
            result += self.solve(i,memo,forget,delay)
        memo[day] = result
        return memo[day]
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        M =  10**9 + 7
        memo = {}
        total = 0
        start = max(1,n-forget+1)
        end = n + 1
        for d in range(start,end):
            total = (total + self.solve(d,memo,forget,delay)) % M
        return total


       

