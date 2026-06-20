class Solution:
    def reorganizeString(self, s: str) -> str:
        """
        create a frequency map to store the freq of eeach characters
        Put that values into max heap
        """
        sDict = defaultdict(int)
        heap = []
        ans = ""
        maxFreq = 0

        for i in s:
            sDict[i] += 1

        for char, freq in sDict.items():
            ni = -1 * freq
            heapq.heappush(heap, (ni, char))
            maxFreq = max(maxFreq,freq)

        if maxFreq > (len(s) + 1) // 2:
            return ""
        
        prev = None

        while heap:
            curr, char = heapq.heappop(heap)

            ans += char
            curr += 1

            if prev:
                heapq.heappush(heap, prev)

            if (-1 * curr) > 0:
                prev = (curr, char)
            else:
                prev = None

        return ans
