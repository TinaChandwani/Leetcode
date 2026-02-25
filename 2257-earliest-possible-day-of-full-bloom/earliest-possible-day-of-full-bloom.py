class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        bloom = sorted(zip(growTime,plantTime),reverse= True)
        days = 0
        max_days = 0
        # print(bloom) [(3, 4), (2, 1), (1, 3)]

        for i in bloom:
            plant = i[1]
            grow = i[0]
            days += plant
            max_days = max(max_days,days+grow)
        return max_days



        