class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        '''
        Applying BS
        '''
        l = 1
        r = max(piles)

        while l < r:
            m = l + (r-l) // 2
            time = 0
            for i in piles:
                b = ceil(i / m)
                time += b
            if time <= h:
                r = m
            else:
                l = m + 1
        
        return r