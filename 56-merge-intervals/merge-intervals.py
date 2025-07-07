class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)
        intervals.sort(key = lambda x:x[0])
        if n == 1:
            return intervals
        merged = []
        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append([interval[0],interval[1]])
            else:
                merged[-1][1] = max(merged[-1][1],interval[1])
        return merged