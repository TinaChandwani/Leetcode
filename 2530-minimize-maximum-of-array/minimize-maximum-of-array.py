class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        def isValid(maxElement):
            arr = nums[:]
            buffer = 0
            for i in range(len(arr)-1):
                if arr[i] > maxElement:
                    return False
                buffer = maxElement - arr[i]
                arr[i+1] = arr[i+1] - buffer
            return arr[len(arr)-1] <= maxElement
        
        l = 1
        r = max(nums)
        ans = 0

        while l <= r:
            m = l + (r-l) // 2
            if isValid(m):
                ans = m
                r = m - 1
            else:
                l = m + 1

        return ans