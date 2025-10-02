class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        '''
        Basically to find median of two sorted array meaning to decide where to cut in both the arrays so we get the median
        1) First think of about the condition where the cut will either land on the median or the median is after the cut (odd or even for both it should be the condition) => T = (m+n) then => L = (T + 1) // 2
        2) so in order to get this boundary if we take i elemets from left then how many elements from right should we take => (L-i)
        3) Then think about the boundaries L1,L2,R1,R2:
            So L1 is the last element in nums1
            R1 - first element in nums1
            L2 - last element in nums2
            R2- first element in nums2
        4) Think of the inequalities between these boundaries 
        ===> L1 <= R2 and L2 <= R1
        5) If L1>R2 ==> then we move left
        6) If L2 > R1 ==> we move right
        7) Do a binary search on smaller array, so if we take m from nums1 then we will take T-m elements from nums2. then check for condition if L1 > R2 yes then move left else move right, if nothing of that is the case then return
        '''

        if len(nums1) >= len(nums2) :
            nums1,nums2 = nums2,nums1
        n, m = len(nums1), len(nums2)
        t = m + n
        l = 0
        r = n
        L = (t+1) // 2
        while r >= l:
            mid = (l+r)//2
            j = L - mid
            if mid > 0:
                l1 = nums1[mid-1]
            else:
                l1 = float('-inf')
            if mid < n:
                r1 = nums1[mid]
            else:
                r1 = float('inf')
            if j > 0:
                l2 = nums2[j-1]
            else:
                l2 = float('-inf')
            if j < m:
                r2 = nums2[j]
            else:
                r2 = float('inf')
            
            if l1 > r2:
                # Shift left
                r = mid - 1
            elif l2 > r1:
                # Shift Right
                l = mid + 1
            else:
                if t % 2 == 0:
                    return (max(l1,l2) + min(r1,r2)) / 2.0
                else:
                    return float(max(l1,l2))
        return -1

            