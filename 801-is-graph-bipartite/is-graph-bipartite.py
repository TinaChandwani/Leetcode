class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        '''
        IF you want to color the graph using two colors =>
        No adjacent colors having the same colors
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
            color[start] = 1

            while q:
                node = q.pop()
                for i in adj[node]:
                    if color[i] == -1:
                        # Not visited, assign color and add in queue
                        color[i] = 1 - color[node]
                        q.append(i)
                    else:
                        if color[node] == color[i]:
                            return False
        return True



