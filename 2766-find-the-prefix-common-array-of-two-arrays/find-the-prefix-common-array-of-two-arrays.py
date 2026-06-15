class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        setA = set(A)
        i = len(A) - 1
        res = [0]*(len(A))

        while i >= 0:
            ctr = 0
            for j in range(i+1):
                if B[j] in setA:
                    ctr += 1
            res[i] = ctr
            setA.remove(A[i])
            i -= 1
        
        return res
