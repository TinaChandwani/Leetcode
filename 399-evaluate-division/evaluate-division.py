class Solution:

    def findDivision(self,start,dest,adj):
        # {'a': [('b', 2.0)], 'b': [('c', 3.0)]})
        # start : b and dest : a
        if start not in adj or dest not in adj:
            return -1.0
        
        if start == dest:
            return 1.0

        q = deque()
        q.append((start,1.0)) # node, val
        visit = set()

        while q:
            node,val = q.popleft()
            if node == dest:
                return val
            if node in visit:
                continue
            visit.add(node)
            for n in range(len(adj[node])):
                element = adj[node][n][0] # b
                ele_value = adj[node][n][1] # 2.0
                if element == dest:
                    return val * ele_value
                if element in visit:
                    continue
                prod = val * ele_value
                q.append((element,prod))
        
        return -1.0

         


    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        adj = defaultdict(list)
        ans = []

        # build a adj list
        for e in range(len(equations)):
            i,j = equations[e][0], equations[e][1]
            adj[i].append((j,values[e]))
            adj[j].append((i,1 / values[e]))
        
        print(adj)
        
        
        for q in range(len(queries)):
            path = self.findDivision(queries[q][0],queries[q][1],adj)
            ans.append(path)
        
        return ans




