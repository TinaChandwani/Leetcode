class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        
        def backtrack(idx,buildings,count):
            if idx >= len(requests):
                for i in buildings:
                    if i != 0:
                        return 0
                return count
            
            f,t = requests[idx][0], requests[idx][1]

            buildings[f] -= 1
            buildings[t] += 1

            take = backtrack(idx + 1, buildings, count + 1)

            buildings[f] += 1
            buildings[t] -= 1

            skip = backtrack(idx + 1, buildings, count)

            return max(take,skip)
        
        buildings = [0] * n

        return backtrack(0,buildings,0)


        


