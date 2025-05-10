class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mpp1 = defaultdict(list)
        mpp2 = defaultdict(list)
        leng = len(s)

        if len(s) != len(t):
            return False
        
        for i in range(leng):
            mpp1[s[i]].append(i)
            mpp2[t[i]].append(i)

        if len(mpp1) == len(mpp2):
            if(list(mpp1.values()) == list(mpp2.values())):
                return True
        return False
        
