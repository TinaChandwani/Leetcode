class RandomizedSet:

    def __init__(self):
        self.dict1 = {}
        self.arr1 = list()
        

    def insert(self, val: int) -> bool:
        if val not in self.dict1:
            self.arr1.append(val)
            self.dict1[val] = len(self.arr1) - 1
            return True
        return False



    def remove(self, val: int) -> bool:
        if val not in self.dict1:
            return False
        index = self.dict1[val]
        last_ele = self.arr1[-1]

        # Swap element at the arr1[index] to last element
        self.arr1[index] = last_ele
        self.dict1[last_ele] = index

        # Delete the last element in the array and from dictionary
        self.arr1.pop()
        del self.dict1[val]
        return True
        

    def getRandom(self) -> int:
        return self.arr1[random.randint(0,len(self.arr1) - 1)]



# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()