class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        indegree = [0] * numCourses
        q = deque()
        count = 0

        for i, j in prerequisites:
            adj[j].append(i)
            indegree[i] += 1
        
        for k in range(numCourses):
            if indegree[k] == 0:
                q.append(k)
        
        while q:
            node = q.popleft()
            count += 1

            for n in adj[node]:
                indegree[n] -= 1
                if indegree[n] == 0:
                    q.append(n)

        return count == numCourses