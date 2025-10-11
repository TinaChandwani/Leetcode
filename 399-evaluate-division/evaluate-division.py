class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        '''
        Create a graph where the characters in the equations are nodes 
        and values are the values a-2-> b -3->c so on...
        so create a adjacency list for the above graph and do bfs on the
        queries list
        '''
        # Creating Adjacency List (Hashmap)
        adj = {}
        for i in range(len(equations)):
            a = equations[i][0]
            b = equations[i][1]
            if a not in adj:
                adj[a] = []
            adj[a].append((b,values[i]))
            if b not in adj:
                adj[b] = []
            adj[b].append((a,(1.0 / values[i])))
        
        print(f'adj {adj}')

        def bfs(i,j):
            print(f'i {i} and j {j}')
            # i = a and j = c
            if i not in adj or j not in adj:
                return -1.0
            if i == j:
                return 1.0
            q = deque() #(node,val)
            q.append([i,1.0])
            visit = set() # a b c
            while q:
                node,val = q.popleft() # c, 12
                if node == j:
                    return val
                if node in visit:
                    continue
                visit.add(node)
                for nodes in range(len(adj[node])):
                    element = adj[node][nodes][0] # d
                    element_value = adj[node][nodes][1] #20
                    if element == j:
                        prod = val * element_value
                        return prod
                    if element in visit:
                        continue
                    prod = val * element_value # 240
                    q.append([element,prod])
                    
            return -1.0
        # Write BFS on the list
        ans = []
        for query in range(len(queries)):
            i = queries[query][0]
            j = queries[query][1]
            output = bfs(i,j)
            ans.append(output)
        return ans

       
                    



                