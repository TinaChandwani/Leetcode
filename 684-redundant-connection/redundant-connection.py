class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        '''
        Solving using Union Find
        '''
        n = len(edges)
        parent = [0] * (n+1)
        rank = [0] * (n+1)
        for i in range(n+1):
            parent[i] = i
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
                elif rank[y_root] < rank[x_root]:
                    parent[y_root] = x_root
                else:
                    parent[y_root] = x_root
                    rank[x_root] += 1

    
        for i in edges:
            u = i[0]
            v = i[1]
            if find(u) == find(v):
                return [u,v]
            union(u,v)
    
