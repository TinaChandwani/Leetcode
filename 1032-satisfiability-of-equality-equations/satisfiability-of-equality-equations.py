class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        '''
        Solving using Union Find. I
        '''
        def find(x):
            if x != parentDict[x]:
                parentDict[x] = find(parentDict[x])
            return parentDict[x]
        def union(x,y):
            xR = find(x)
            yR = find(y)
            if xR == yR:
                return True
            else:
                parentDict[yR] = xR
            return False
        
        parentDict = {}
        inequal = []
        
        n = len(equations)
        for i in range(n):
            eq = equations[i]
            u = eq[0]
            v = eq[3]
            if u not in parentDict:
                parentDict[u] = u
            if v not in parentDict:
                parentDict[v] = v
            sign = eq[1]

            if sign == '=':
                union(u,v)
            else:
                inequal.append([u,v])

        for i,j in inequal:
            if find(i) == find(j):
                return False
        return True  