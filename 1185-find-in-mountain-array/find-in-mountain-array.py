# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        '''
        1. Find Peak Index (idx)
        2. Binary Search from 0 to idx and (idx+1) to (n-1)
        '''
        def findPeak(l,r):
            while l < r:
                m = l + (r-l) // 2
                if mountainArr.get(m) < mountainArr.get(m + 1):
                    l = m + 1
                else:
                    r = m 
            return l
        
        def binarySearch(l,r,direction):
            found = False
            while l <= r:
                m = l + (r-l) // 2
                if mountainArr.get(m) == target:
                    found = True
                    return (found,m)
                elif mountainArr.get(m) < target:
                    if direction == 1:
                        l = m + 1
                    else:
                        r = m - 1
                else:
                    if direction == 1:
                        r = m - 1
                    else:
                        l = m + 1
            return (found,l)
        
        n = mountainArr.length()
        peak = findPeak(0,n - 1)
        iffound, idx = binarySearch(0,peak,1)
        if iffound == True:
            return idx
        iffound, idx = binarySearch(peak + 1, n - 1, -1)
        if iffound == True:
            return idx
        
        return -1