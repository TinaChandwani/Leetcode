class TimeMap:

    def __init__(self):
        self.tDict = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.tDict[key].append([timestamp,value])
        

    def get(self, key: str, timestamp: int) -> str:
        l = 0 
        values = self.tDict[key]
        r = len(values) - 1

        while l <= r:
            m = l + (r-l) // 2
            t = values[m][0]
            v = values[m][1] 
            if timestamp == t:
                return v
            elif timestamp < t:
                r = m - 1
            else:
                l = m + 1
        if r < 0:
            return ""
        return values[r][1]   
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)