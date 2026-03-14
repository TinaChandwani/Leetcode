class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l = 0
        r = 0
        maxLen = 0
        n = len(fruits)
        active = defaultdict(int)

        while r < n:
            active[fruits[r]] += 1
            while len(active) > 2:
                active[fruits[l]] -= 1
                if active[fruits[l]] == 0:
                    del active[fruits[l]]
                l += 1
            maxLen = max(maxLen,r-l+1)
            r += 1
        
        return maxLen