class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        candy = n
        i = 1

        while i < n:
            # Flat surface
            if ratings[i] == ratings[i-1]:
                i += 1
                continue

            # Increasing Slope
            peak = 0
            while ratings[i] > ratings[i-1]:
                peak += 1
                candy += peak
                i += 1
                if i == n:
                    return candy
            
            # Decreasing Slope
            dip = 0
            while i < n and ratings[i] < ratings[i-1]:
                dip += 1
                candy += dip
                i += 1

            candy -= min(dip,peak)
        
        return candy


        