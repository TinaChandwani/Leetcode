class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        size = 0
        ans = []
        active = set()
        pDict = defaultdict(int)
        
        for _ in s:
            pDict[_] += 1
        
        for i in s:
            pDict[i] -= 1
            active.add(i)
            size += 1
            if pDict[i] == 0:
                active.remove(i)
            if len(active) == 0:
                ans.append(size)
                size = 0
        return ans
                    