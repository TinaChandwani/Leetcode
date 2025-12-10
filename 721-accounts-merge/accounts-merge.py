class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]   

        def union(x,y):
            xRoot = find(x)
            yRoot = find(y)
            if xRoot == yRoot:
                return
            else:
                parent[yRoot] = xRoot
            
        parentDict = {} # Email -> Acc Index
        n = len(accounts)
        parent = {i: i for i in range(n)}
        for i,email in enumerate(accounts):
            for e in email[1:]:
                if e not in parentDict:
                    parentDict[e] = i
                else:
                    union(i,parentDict[e])

        emailGroup = defaultdict(list)

        for e,i in parentDict.items():
            root = find(i)
            emailGroup[root].append(e)
        
        result = []
        for root_idx, emails in emailGroup.items():
            name = accounts[root_idx][0]
            result.append([name] + sorted(emails))

        return result
