class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # Iterative
        l = 0
        n = len(nums)
        r = n - 1
        ans = []
        if n == 1 and target == nums[0]:
            return [0,0]
        while r >= l:
            m = (l + r) // 2
            print(f'm = {m}')
            if target == nums[m]:
                print('found')
                first = m
                last = m
                while m > 0 and nums[m-1] == target :
                    print(f'm-1 = {m-1}')
                    first = m - 1
                    m = m - 1
                while m < (n-1) and nums[m+1] == target :
                    print(f'm+1 = {m+1}')
                    last = m + 1
                    m = m + 1
                print(f'ans {[first,last]}')
                return [first,last]
            if target > nums[m]:
                l = m + 1
            else:
                r = m - 1
        return [-1,-1]

