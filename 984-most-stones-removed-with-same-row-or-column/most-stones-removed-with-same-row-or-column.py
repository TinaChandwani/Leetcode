class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        '''
        Solving using Union Find in O(N) time complexity

        '''
        parent = {}

        def find(x):
            if x not in parent:
                parent[x] = x
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x,y):
            root_x = find(x)
            root_y = find(y)
            if root_x == root_y:
                return
            else:
                parent[root_y] = root_x
        
        for i in stones:
            u = i[0]
            v = i[1]
            union(('r',u),('c',v))
        
        roots = set()
        for i in range(len(stones)):
            roots.add(find(('r',stones[i][0])))
        return len(stones) - len(roots)