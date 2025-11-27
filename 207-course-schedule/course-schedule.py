class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        '''
        Using Kahn Algorithm BFS
        Use the In degree concept
        '''
        indegree = [0] * numCourses
        visit = set()
        adj = defaultdict(list)
        # Create Adj and populate the indegree array
        for i, j in prerequisites:
            adj[i].append(j)
            indegree[j] += 1
        for i in range(numCourses):
            if i in visit:
                continue
            q = deque()

            for d in range(len(indegree)):
                if indegree[d] == 0 and d not in visit:
                    q.append(d)
            while q:
                node = q.popleft()
                visit.add(node)
                for n in adj[node]:
                    indegree[n] -= 1
                    if indegree[n] == 0:
                        q.append(n)
        for v in range(numCourses):
            if v not in visit:
                return False
        return True
                

        