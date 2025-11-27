class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        '''
        Basically here we need to rotate the direction of the arrow
        in the graph and write topological ordering for the node
        '''
        n = len(graph)
        visit = set()
        ans = []
        indegree = [0] * n
        adj = defaultdict(list)
        for i in range(n):
            l = graph[i]
            for j in l:
                adj[j].append(i)
                indegree[i] += 1
        q = deque()
        for d in range(n):
            if indegree[d] == 0 and d not in visit:
                q.append(d)
        while q:
            node = q.pop()
            visit.add(node)
            ans.append(node)
            for j in adj[node]:
                indegree[j] -= 1
                if indegree[j] == 0:
                    q.append(j)
        out = sorted(ans)    
        return out
            
        
        