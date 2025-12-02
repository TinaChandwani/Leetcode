class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        '''
        Solving using DFS
        '''
        restricted = set(restricted)
        visit = set()
        adj = defaultdict(list)
        count = 1
        q = deque()
        for i in edges:
            u = i[0]
            v = i[1]
            adj[u].append(v)
            adj[v].append(u)
        q.append(0) # Start Node
        print(f'adj {adj}')
        while q:
            node = q.popleft()
            visit.add(node)
            for j in adj[node]:
                if j not in restricted and j not in visit:
                    count += 1
                    q.append(j)
        
        return count

        