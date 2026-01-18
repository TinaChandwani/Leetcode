class MyHashMap:

    def __init__(self):
        self.buckets = 1009
        self.hashMap = [[] for j in range(self.buckets)]
    
    def getKey(self,key: int):
        return key % self.buckets

    def put(self, key: int, value: int) -> None:
        index = self.getKey(key)
        present = False
        for k in range(len(self.hashMap[index])):
            if self.hashMap[index][k][0] == key:
                present = True
                self.hashMap[index][k][1] = value
                return
        if not present:
            self.hashMap[index].append([key,value])

    def get(self, key: int) -> int:
        index = self.getKey(key)
        for k,v in self.hashMap[index]:
            if k == key:
                return v
        return -1
        

    def remove(self, key: int) -> None:
        index = self.getKey(key)
        if len(self.hashMap[index]) > 0:
            for i in range(len(self.hashMap[index])):
                if self.hashMap[index][i][0] == key:
                    del self.hashMap[index][i]
                    return
                
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)