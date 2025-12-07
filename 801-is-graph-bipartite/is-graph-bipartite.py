class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        '''
        IF you want to color the graph using two colors =>
        No adjacent colors having the same colors

        Time Complexity:
        1. Each node is processed at most once
        2. Each edge is checked at most twice (u ->v and v ->u in 
        adj list)
        --> O(V+E)
        DFS
        '''
        # Red = 1 white = 0
        n = len(graph)
        color = [-1] * n
        adj = defaultdict(list)
        

        # Create Adj list
        for g in range(n):
            for no in graph[g]:
                adj[g].append(no)

        for start in range(n):
            if color[start] != -1:
                continue
            
            q = deque()
            q.append(start)
            color[start] = 0

            while q:
                node = q.popleft()
                for i in adj[node]:
                    if color[i] == -1:
                        # Not visited, assign color and add in queue
                        color[i] = 1 - color[node]
                        q.append(i)
                    else:
                        if color[node] == color[i]:
                            return False
        return True



