class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        '''
        '''
        l = 1
        r = min(time) * totalTrips 

        while l < r:
            m = l + (r-l)// 2
            trips = 0

            for i in range(len(time)):
                t = m // time[i]
                trips += t
            
            if trips >= totalTrips:
                r = m
            else:
                l = m + 1
        
        return l