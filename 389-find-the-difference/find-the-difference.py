class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        if len(s) == 0:
            return t

        count = defaultdict(int)

        for i in s:
            count[i] += 1

        
        for j in t:
            count[j] -= 1
            if count[j] < 0:
                return j
        
       
        