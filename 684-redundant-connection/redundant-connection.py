class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        '''
        Solving using Union Find
        '''
        n = len(edges)
        parent = [0] * (n+1)
        for i in range(n+1):
            parent[i] = i
        def find(x):
            while x != parent[x]:
                x = parent[x]
            return x
         
        def union(x,y):
            x_root = find(x)
            y_root = find(y)
            if x_root == y_root:
                return 
            else:
                parent[y_root] = x_root

    
        for i in edges:
            u = i[0]
            v = i[1]
            if find(u) == find(v):
                return [u,v]
            union(u,v)
    
