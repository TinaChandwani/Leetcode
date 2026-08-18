class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        indegree = [0] * numCourses
        q = deque()
        count = 0
        res = []

        for i,j in prerequisites:
            adj[j].append(i)
            indegree[i] += 1
        
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        
        while q:
            node = q.popleft()
            res.append(node)
            count += 1

            for n in adj[node]:
                indegree[n] -= 1
                if indegree[n] == 0:
                    q.append(n)
        
        if count == numCourses:
            return res
        else:
            return []
