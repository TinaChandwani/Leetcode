class Solution:
    def magnificentSets(self, nei: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        color = [-1] * (nei+1)
        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        components = []
        # To check if the graph is bipartite or not 
        # If it is NOT Bipartite then return -1
        for start in range(1,nei+1):
            if color[start] != -1:
                continue
            q = deque()
            q.append(start)
            comp_nodes = []
            comp_nodes.append(start)
            color[start] = 0
            while q:
                node = q.popleft()
                for n in adj[node]:
                    if color[n] == -1:
                        # Not visited before
                        color[n] = 1 - color[node]
                        q.append(n)
                        comp_nodes.append(n)
                    elif color[n] == color[node]:
                        return -1
            components.append(comp_nodes)

        def bfs_helper(nodes):
            queue = deque()
            queue.append(nodes)
            dist = {nodes : 1}
            max_level = 1
            while queue:
                no = queue.popleft()
                for j in adj[no]:
                    if j not in dist:
                        # Not Visited
                        dist[j] = 1 + dist[no]
                        queue.append(j)
                        max_level = max(max_level,dist[j])
            
            return max_level
        
        ans = 0

        for a in components:
            best = 0
            for b in a:
                best = max(best,bfs_helper(b))
            ans += best
        return ans