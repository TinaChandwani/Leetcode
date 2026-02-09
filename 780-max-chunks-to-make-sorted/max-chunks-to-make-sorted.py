class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        '''
        '''
        chunks = 0
        i = 0
        currmax = 0
        while i < len(arr):
            currmax = max(currmax,arr[i])
            if currmax == i:
                chunks += 1
            i += 1
        return chunks

