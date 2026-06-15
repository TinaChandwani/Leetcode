class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        hashMap = defaultdict(int)
        res = [0]
        
        for i in range(len(A)):
            ctr = 0
            hashMap[A[i]] += 1
            if hashMap[A[i]] == 2:
                ctr += 1
            hashMap[B[i]] += 1
            if hashMap[B[i]] == 2:
                ctr += 1
            res.append(res[-1] + ctr)
        
        return res[1:]
            
            

        

