class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2,nums1)
        
        m = len(nums1)
        n = len(nums2)

        l = 0
        r = m

        while l <= r:
            Px = l + (r-l)// 2 # mid
            Py = ((m+n+1) // 2) - Px

            # Left wale
            if Px == 0:
                x1 = float('-inf')
            else:
                x1 = nums1[Px-1]

            if Py == 0:    
                x2 = float('-inf')
            else: 
                x2 = nums2[Py-1]
            
            # Right wale
            if Px == m:
                x3 = float('inf')
            else:
                x3 = nums1[Px]
            
            if Py == n:
                x4 = float('inf')
            else:
                x4 = nums2[Py]    
            
            if x1 <= x4 and x2 <= x3:
                if (m+n) % 2 == 0:
                    return (max(x1,x2) + min(x3,x4)) / 2.0
                else:
                    return max(x1,x2)
            
            if x1 > x4:
                r = Px - 1
            else:
                l = Px + 1
        
        return -1
         
