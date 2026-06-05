class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        '''
        BFS
        starting from node 0 check it's neigbours :
            - if the nighbours can access 0 then okay else count += 1
            - then from it's neigbours check if their neigbours can access negibours
        Recursive code
        '''

        edges = { (a,b) for a,b in connections }
        visit = set()
        visit.add(0)
        nDict = defaultdict(list)
        q = deque()
        q.append(0)
        ans = 0

        # Adjancency List (consider Bidirectional)
        for i,j in connections:
            nDict[i].append(j)
            nDict[j].append(i)
        
        
        while q:
            node = q.popleft()
            for a in nDict[node]:
                if a not in visit:
                    visit.add(a)
                    if (a,node) not in edges:
                        ans += 1
                    q.append(a)
        
        return ans


