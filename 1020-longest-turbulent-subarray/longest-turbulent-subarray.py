class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n = len(arr)
        if n == 1:
            return 1
        else:
            diff = arr[1] - arr[0]
            if diff > 0:
                sign = 0
                ans = 2
            elif diff < 0:
                sign = 1
                ans = 2
            else:
                sign = -1
                ans = 1
        # 0 = positive | 1 = negative
        i = 1
        maxans = ans

        while (i + 1) < n:
            diff = arr[i+1] - arr[i]
            if diff == 0:
                sign = -1
                ans = 1
            elif diff > 0:
                # positive difference
                if sign == 1:
                    ans += 1
                else:
                    ans = 2
                sign = 0
            elif diff < 0:
                # negative difference
                if sign == 0:
                    ans += 1
                else:
                    ans = 2
                sign = 1
            maxans = max(maxans,ans)
            i += 1
        return maxans