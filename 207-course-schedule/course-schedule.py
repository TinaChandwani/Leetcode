class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Create an adj list
        # I need to reset inRecursion call after every node finishes
        adj = defaultdict(list)
        for i,j in prerequisites:
            adj[i].append(j)
        visit = set()
        for i in range(numCourses):
            if i in visit:
                continue
            q = deque()
            inRecursion = [False] * numCourses
            q.append((i,True)) # node, enter state
            while q:
                node,enter = q.pop()
                if enter:
                    visit.add(node)
                    if inRecursion[node]:
                        return False
                    inRecursion[node] = True
                    q.append((node,False))
                    for j in adj[node]:
                        if j not in visit:
                            q.append((j,True))
                        elif inRecursion[j] == True:
                            return False   
                else:
                      inRecursion[node] = False
        return True


        
         