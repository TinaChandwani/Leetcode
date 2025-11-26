class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        '''
        Solve using Union Find
        Union Find is used to see if two components belong to the 
        same group
        '''
        n = len(stones)     
        parent = [i for i in range(n)]
        
        print(f'parent {parent}')

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
                parent[y_root] = x_root
    
        for i in range(n):
            u,v = stones[i]
            for j in range(i+1,n):
                u1,v1 = stones[j]
                if u1 == u or v == v1:
                    union(i,j)
            
        root = set()
        for i in range(n):
            root.add(find(i))
        
        c = len(root)
        return n - c
        
