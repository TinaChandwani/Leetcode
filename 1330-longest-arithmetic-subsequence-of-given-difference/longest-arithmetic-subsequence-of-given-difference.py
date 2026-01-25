class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        '''
        Create a map stored the difference
        '''
        arrDict = defaultdict(int)
        for i in arr:
            p = i - difference
            if p in arrDict:
                arrDict[i] = arrDict[p] + 1
            else:
                arrDict[i] = 1
        return max(arrDict.values())