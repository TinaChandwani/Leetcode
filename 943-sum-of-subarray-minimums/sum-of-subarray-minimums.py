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
        while s1:
            p = s1.pop()
            nsr[p] = n - p  
        
        # NSL
        s2 = []
        nsl = [0] * n
        for j in range(n):
            while s2 and arr[s2[-1]] >= arr[j]:
                s2.pop()
            nsl[j] = j - s2[-1] if s2 else j + 1
            s2.append(j)
        print(f'nsr {nsr}')
        print(f'nsl {nsl}')
        for k in range(n):
            l = nsr[k]
            r = nsl[k] 
            total = l * r * arr[k]
            ans += total

        return ans % mod