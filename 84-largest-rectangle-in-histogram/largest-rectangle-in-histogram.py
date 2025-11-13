class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        '''
        Use a stack when:
        ✔ Elements depend on previous elements
        ✔ You care about “first smaller” or “first bigger”
        ✔ A decreasing element should “trigger” some calculation
        ✔ You need to know how far something can stretch left/right
        ✔ You process items and “undo” earlier ones 
        when a condition breaks
        These problems are designed for stacks.
        This is a Monotonic Stack problem
        '''
        ''' 
        ns = Find the next smaller element
        ps = Find the previous smaller element
        Area = Height[i] * (ns-ps - 1)
        '''
        # Find the Next Smaller Element 
        n = len(heights)
        nse = [n] * n
        stack1 = []

        for i in range(n-1,-1,-1):
            while stack1 and heights[stack1[-1]] >= heights[i]:
                stack1.pop()
            if stack1:
                nse[i] = stack1[-1]
            stack1.append(i)
        
        print(f'nse {nse}')

        # Find the previous Smaller Element
        stack2 = []
        pse = [-1] * n

        for j in range(n):
            while stack2 and heights[stack2[-1]] >= heights[j]:
                stack2.pop()
            if stack2:
                pse[j] = stack2[-1]
            stack2.append(j)
        
        print(f'pse {pse}')
        
        # Find the area
        max_area = 0

        for k in range(n):
            height = heights[k]
            width = (nse[k] - pse[k] - 1)
            area = height * width
            max_area = max(max_area,area)
        
        return max_area

