class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        curr = 1
        prev = 0
        run = 1
        i = 1
        n = len(arr)
        ans = 1
        while i < n:
            if arr[i] < arr[i-1]:
                curr = -1
            elif arr[i-1] < arr[i]:
                curr = 1
            else:
                curr = 0
            
            if curr == 0:
                run = 1
            elif prev == 0 or curr == -prev:
                run += 1
            else:
                run = 2
            
            ans = max(ans,run)
            prev = curr
            i += 1
        return ans
