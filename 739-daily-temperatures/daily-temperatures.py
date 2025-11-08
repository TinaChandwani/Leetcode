class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        '''
        This is a Monotonic stack problem : the stack will either have 
        decreasing or non-decreasing order
        '''
        n = len(temperatures)
        if n == 1:
            return [0]
        ans = [0] * n
        stack = []
        for i in range(n):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                pop = stack.pop()
                ans[pop] = i - pop
            stack.append(i)
    
        # if stack:
        #     zero = len(stack)
        #     ans = ans + [0] * zero
        
        return ans