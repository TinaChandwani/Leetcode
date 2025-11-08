class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        '''
        Using Stacks the time complexity becomes n + m
        brute force - n * m
        '''
        ansDict = {}
        stack = []
        n = len(nums2)
        ans = []

        for i in range(n):
            while stack and stack[-1] < nums2[i]:
                prev = stack.pop()
                ansDict[prev] = nums2[i]
            stack.append(nums2[i])
        
        for j in nums1:
            if j in ansDict.keys():
                output = ansDict[j]
            else:
                output = -1
            ans.append(output)
        
        return ans
        