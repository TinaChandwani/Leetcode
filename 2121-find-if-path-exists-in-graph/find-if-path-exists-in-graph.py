class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        '''
        Solving Using Union Find
        So Basically Union Find tells us if two nodes belong to the same group,
        if they do then there exist a valid path in the graph else no
        '''
        parent = [0] * n
        for i in range(n):
            parent[i] = i
        rank = [0] * n

        def find(x):
            while x != parent[x]:
                x = find(parent[x])
            return parent[x]
        
        def union(x,y):
            x_root = find(x)
            y_root = find(y)
            if x_root == y_root:
                return
            else:
                if rank[x_root] < rank[y_root]:
                    parent[x_root] = y_root
                elif rank[x_root] > rank[y_root]:
                    parent[y_root] = x_root
                else:
                    parent[y_root] = x_root
                    rank[x_root] += 1
        
        for j in edges:
            u = j[0]
            v = j[1]
            union(u,v)
        
        return find(source) == find(destination)