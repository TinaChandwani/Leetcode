class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        '''
        Classic Bipartite Question => Solving using BFS
        '''
        adj = defaultdict(list)
        color = [-1] * (n+1)
        # Create adj in directed graph
        for a,b in dislikes:
            # a -> b
            adj[a].append(b)
            adj[b].append(a)
        
        for start in range(n):
            if color[start] != -1:
                continue
            q = deque()
            q.append(start)
            color[start] = 1
            while q:
                node = q.popleft()
                for i in adj[node]:
                    if color[i] == color[node]:
                        return False
                    else:
                        if color[i] == -1 :
                            # Not visited
                            color[i] = 1 - color[node]
                            q.append(i)
        return True
        
        