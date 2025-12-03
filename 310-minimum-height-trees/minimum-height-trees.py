class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        '''
        Observations:
        1) Choose central nodes
        2) You will always get max two root labels
        Time Complexity -> O(V+E)
        '''
        if len(edges) == 0:
            return [0]
        # Create adj
        indegree = [0] * n
        q = deque()
        remain = n

        adj = defaultdict(list)
        for i,j in edges:
            adj[i].append(j)
            adj[j].append(i)
            indegree[i] += 1
            indegree[j] += 1

        for d in range(n):
            if indegree[d] == 1:
                # It is a leaf node
                q.append(d)

        while remain > 2:
            # basically we need to do BFS traversal
            l = len(q)
            for _ in range(l):
                n = q.popleft()
                remain -= 1
                for j in adj[n]:
                    indegree[j] -= 1
                    if indegree[j] == 1:
                        q.append(j)
        ans = []
        while q:
            n = q.popleft()
            ans.append(n)
        return ans
        



        