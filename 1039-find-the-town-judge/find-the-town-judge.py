class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
            '''
            It's a directed graph where I calculate indegree and
            outdegree
            '''
            indegree = [0] * (n + 1)
            outdegree = [0] * (n + 1)

            for i,j in trust:
                indegree[j] += 1
                outdegree[i] += 1
            
            for d in range(1,n+1):
                if outdegree[d] == 0 and indegree[d] == n - 1:
                    return d
            return -1
