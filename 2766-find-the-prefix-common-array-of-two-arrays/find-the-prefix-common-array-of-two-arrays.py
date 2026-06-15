class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        countMap = defaultdict(int)
        res = 0
        n = len(A)
        ans = []

        for i in range(n):
            n1,n2 = A[i],B[i]
            countMap[n1] += 1
            countMap[n2] += 1
            if countMap[n1] == 2:
                res +=1 
            if n1 != n2 and countMap[n2] == 2:
                res += 1
            ans.append(res)
        
        return ans
