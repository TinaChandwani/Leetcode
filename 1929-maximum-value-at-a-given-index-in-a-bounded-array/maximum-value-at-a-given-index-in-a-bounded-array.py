class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        def getSum(count,x):
            if count <= x:
                return ((2 * x - count + 1) * count) // 2
            return (x * (x + 1)) // 2 + (count - x)
        
        l = 1
        r = maxSum
        ans = 1

        while l <= r:
            m = l + (r-l) // 2
            left_count = getSum(index,m-1)
            right_count = getSum(n-index-1,m-1)
            total_sum = left_count + m + right_count
            if total_sum > maxSum:
                r = m - 1
            else:
                ans = m
                l = m + 1
        
        return ans