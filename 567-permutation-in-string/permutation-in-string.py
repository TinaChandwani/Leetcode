class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        l = 0
        r = 0
        n = len(s2)
        s1Dict = {}
        s2Dict = defaultdict(int)

        for i in s1:
            if i in s1Dict:
                s1Dict[i] += 1
            else:
                s1Dict[i] = 1

        while r < n:
            if s2[r] in s1Dict:
                s2Dict[s2[r]] += 1
            
            while r - l + 1 > len(s1):
                # Shrink
                if s2[l] in s1Dict:
                    s2Dict[s2[l]] -=1
                    if s2Dict[s2[l]] == 0:
                        del s2Dict[s2[l]]
                l += 1
            
            if s1Dict == s2Dict:
                return True
            
            r += 1
        
        return False
