class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        '''
        Solve using Union Find:
            -> Basically whenever you find a cycle remove it
        '''
     
        parent = [i for i in range(n)]
        rank = [0] * n
        count = 0
        visit = set()
        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x,y):
            root_x =  find(x)
            root_y = find(y)
            if root_x == root_y:
                return False
            else:
                if rank[root_x] < rank[root_y]:
                    parent[root_x] = root_y
                elif rank[root_x] > rank[root_y]:
                    parent[root_y] = root_x
                else:
                    parent[root_y] = root_x
                    rank[root_x] += 1
            return True
        
        i = 0
        connected = set()
        while i < len(connections):
            u = connections[i][0]
            v = connections[i][1]
            if find(u) == find(v):
                count += 1
                visit.add((u,v))
            if (u,v) not in visit:
                union(u,v)
            i += 1
        # parent_set = set(parent)

        parent_set = set()
        for i in range(n):
            parent_set.add(find(i))

        print(f'parent_set {parent_set}')
        print(f'count {count}')
        if len(parent_set) - 1 > count:
            return -1
        else:
            return len(parent_set)-1

