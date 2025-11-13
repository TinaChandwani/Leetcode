class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        '''
        The whole idea is the smallest possible integer could be
        increasing order of num 
        '''
        n = len(num)
        if n == k:
            return "0"
        stack = []
        ans = ""

        for i in range(n):
            while stack and int(stack[-1]) > int(num[i]) and k != 0:
                prev = stack.pop()
                k -= 1
            stack.append(num[i])
        
        while k > 0 and stack:
            stack.pop()
            k = k - 1
        ans = "".join(stack).lstrip("0")
        if ans:
            return ans
        else:
            return "0"