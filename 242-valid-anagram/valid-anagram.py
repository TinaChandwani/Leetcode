class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter = defaultdict(int)

        if len(s) != len(t):
            return False

        for x in s:
            counter[x] += 1
        
        for x in t:
            counter[x] -= 1
        
        for j in counter.values():
            if j != 0:
                return False
        
        return True