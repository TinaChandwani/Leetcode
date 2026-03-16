class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        ans = 0
        mod = 10**9 + 7
        # NSR
        nsr = [n] * n
        s1 = []
        for i in range(n):
            while s1 and arr[s1[-1]] >= arr[i]:
                p = s1.pop()
                nsr[p] = i - p
            s1.append(i)
        
        # NSL
        s2 = []
        nsl = [-1] * n
        for j in range(n-1,-1,-1):
            while s2 and arr[s2[-1]] > arr[j]:
                p = s2.pop()
                nsl[p] = p - j
            # nsl[j] = j - s2[-1] if s2 else j + 1
            s2.append(j)
        print(f'nsr {nsr}')
        print(f'nsl {nsl}')
        for k in range(n):
            l = nsr[k] if nsr[k] != n else n - k 
            r = nsl[k] if nsl[k] != -1 else k + 1
            total = l * r * arr[k]
            ans += total

        return ans % mod