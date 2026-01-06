class RandomizedSet:

    def __init__(self):
        self.rDict = defaultdict(int)
        self.arr = list()
        

    def insert(self, val: int) -> bool:
        if val in self.rDict:
            return False
        self.arr.append(val)
        self.rDict[val] = len(self.arr) - 1
        return True
        
    def remove(self, val: int) -> bool:
        if val not in self.rDict:
            return False
        last_ele = self.arr[-1]
        index = self.rDict[val]
        # Swap two elements
        self.arr[index] = last_ele
        self.rDict[last_ele] = index

        # Delete from arr and dictionary
        del self.rDict[val]
        self.arr.pop()
        return True

    def getRandom(self) -> int:
        return random.choice(self.arr)

        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()