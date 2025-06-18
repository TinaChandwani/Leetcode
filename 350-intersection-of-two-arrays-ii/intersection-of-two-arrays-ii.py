class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        countDict = defaultdict(int)
        output = []
        
        if len(nums1) > len(nums2):
            nums1,nums2 = nums2,nums1
        for i in nums1:
            countDict[i] += 1
        
        for j in nums2:
            if j in countDict and countDict[j] != 0:
                output.append(j)
                countDict[j] -= 1   
        return output