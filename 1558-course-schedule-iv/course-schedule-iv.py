class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        '''
        Constraints of the problem :
        1) There is no cycle in pre array
        2) ui != vj

        Basically Write the linear ordering or topological sort of the
        entire graph and then check the queries u and v
        '''
        if len(prerequisites) == 0:
            return [False] * len(queries)
        adj = defaultdict(list)
        q = deque()
        tDict = defaultdict(int)
        indegree = [0] * numCourses
        counter = []
        prereq = [set() for i in range(numCourses)]
        ans = []
        
        # create a adj graph (directed graph)
        for i, j in prerequisites:
            adj[i].append(j)
            indegree[j] += 1
        # print(f'adj {adj}')
        print(f'indegree {indegree}')
        # Append in the queue whose indegree is 1
        for d in range(numCourses):
            if indegree[d] == 0:
                q.append(d)
        # Write the topological ordering of the graph
        while q:
            node = q.popleft()
            counter.append(node)
            for nei in adj[node]:
                if nei not in tDict:
                    indegree[nei] -=1
                    prereq[nei].add(node)
                    # Find the pre of the node as well
                    for p in prereq[node]:
                        prereq[nei].add(p)
                    if indegree[nei] == 0:
                        q.append(nei)
        
        print(f'counter {counter}') 
        print(f'prereq {prereq}')

        for qr,rq in queries:
            if qr in prereq[rq]:
                ans.append(True)
            else:
                ans.append(False)
        return ans

