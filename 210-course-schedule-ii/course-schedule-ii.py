class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        '''
        To Print the Topological Ordering
        '''
        indegree = [0] * numCourses
        visit = set()
        ans = []
        adj = defaultdict(list)
        for i,j in prerequisites:
            adj[j].append(i)
            indegree[i] += 1
        print(f'adj {adj}')
        print(f'indegree {indegree}')
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
                ans.append(node)
                for n in adj[node]:
                    indegree[n] -= 1
                    if indegree[n] == 0:
                        q.append(n)
        if len(visit) != numCourses:
                return [] 
        return ans

        