class Solution:
    def candy(self, ratings: List[int]) -> int:
        total = 1
        n = len(ratings)
        i = 1
        while i < n:
            if ratings[i] == ratings[i-1]:
                total += 1
                i += 1
                continue
            peak = 1
            while i < n and ratings[i] > ratings[i-1]:
                peak += 1
                total += peak
                i += 1
            down = 1
            while i < n and ratings[i] < ratings[i-1]:
                total += down
                down += 1
                i += 1
            if peak < down:
                total += (down - peak)
        
        return total