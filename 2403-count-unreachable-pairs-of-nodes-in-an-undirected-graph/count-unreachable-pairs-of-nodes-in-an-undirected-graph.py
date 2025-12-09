class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x,y):
            xR = find(x)
            yR = find(y)
            if yR == xR:
                return 
            else:
                parent[yR] = xR
        
        parent = [ _ for _ in range(n)]

        for u,v in edges:
            union(u,v)
        
        for i in range(n):
            parent[i] = find(i)
        count = Counter(parent)
        ans = 0
        total = sum(count.values())
        
        for i in count.values():
            print(total)
            total = total - i
            ans += i * total
        return ans

        