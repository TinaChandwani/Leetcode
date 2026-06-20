class Solution:
    def reorganizeString(self, s: str) -> str:
        '''
        create a frequency map to store the freq of eeach characters
        Put that values into max heap
        '''
        sDict = defaultdict(int)
        heap = []
        ans = ""

        for i in s:
            sDict[i] += 1
        
        for char,freq in sDict.items():
            ni = -1 * freq
            heapq.heappush(heap,(ni,char))
        
        while heap:
            first,c = heapq.heappop(heap)
            if (-1 * first) > (len(s) + 1) // 2:
                return ""
            ans += c
            first += 1
            if heap:
                second,c2 = heapq.heappop(heap)
                ans += c2
                second += 1
                if second != 0:
                    heapq.heappush(heap,(second,c2))
            if first != 0:
                heapq.heappush(heap,(first,c))

        return ans
            

            