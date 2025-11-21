class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        '''
        Solving using Union Find
        '''
        n = len(isConnected)
        m = len(isConnected[0])
        # Creating parent of each node
        parent = [0] * n
        for i in range(n):
            parent[i] = i
        
        def union(x,y):
            # Merge two groups 
            root_x = find(x)
            root_y = find(y)
            if root_x != root_y:
                parent[root_y] = root_x
            else:
                # the two groups belong together
                return
         
        def find(x):
            # Find which group x belongs to
            while parent[x] != x:
                x = parent[x]
            return x
        
        for i in range(n):
            for j in range(m):
                if isConnected[i][j] == 1:
                    union(i,j)
        
        roots = set()
        # Count the number of provinces
        for i in range(n):
            roots.add(find(i))
        
        return len(roots)
