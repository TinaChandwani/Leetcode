class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        i,j = 1,0
        res = []

        while i < n + 1 and j < len(target):
            if i == target[j]:
                res.append("Push")
                j += 1
            else:
                res.append("Push")
                res.append("Pop")
            i += 1

        return res
