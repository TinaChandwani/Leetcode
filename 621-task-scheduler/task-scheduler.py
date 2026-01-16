import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        countDict = defaultdict(int)
        heap = []
        count = 0
        # Create Map to count frequency of each alphabet
        for i in range(len(tasks)):
            countDict[tasks[i]] += 1
        # Using the frequency of each alphabet, create a max heap
        for alphabet,freq in countDict.items():
            heapq.heappush(heap,(-freq,alphabet))
        
        # the most frequent element would be at heap[0]
        while heap:
            initial_n = n 
            deleteSet = set()
            while initial_n >= 0 :
                if heap:
                    f,l = heapq.heappop(heap)
                    countDict[l] -= 1
                    count += 1
                    if countDict[l] == 0:
                        del countDict[l]
                    else:
                        deleteSet.add(l)
                else:
                    # Count the idle times
                    if countDict:
                        count += 1
                    else:
                        break
                initial_n -= 1
            for j in deleteSet:
                heapq.heappush(heap,(-countDict[j],j))
        return count


