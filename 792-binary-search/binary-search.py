class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Recursive
        def bs(l,r):
            print(f'l {l} and r {r}')
            if l > r:
                return -1
            m = (l + r)// 2
            print(f'm {m}')
            if nums[m] == target:
                return m
            elif target > nums[m]:
                return bs(m+1,r)
            else:
                return bs(l,m-1)
        
        return bs(0,len(nums)-1)
        