class MyHashSet:
    '''
    Hashsets is a collection that stores unique values (no duplicates), supports add(x)
    remove(x) and contains(x) => Does all this operations fast (O(1))

    Use Hash function that maps key -> index

    Hash tables give:
        1. Average Case -> O(1)
        2. Worst Case -> O(N)
    
    If all keys map to the same index, how would you optimize this?
        1. This happens when poor hash function or too many keys compared to buckets
        2. This DOES NOT mean that hashing is broken
        3. Optimization #1 : Better Hash Distribution
            I. If input keys have patterns => collisions explode
            II. Use a large prime number for table size (Prime sizes distribute more evenly)
        4. Optimization # 2: Increase number of buckets
        5. Optimization # 3: Load factor (n/M)
            I. n = number if input elements and M = number of buckets
            II. Rule of Thumb : if load factor > 0.7, performance degrades
        6. Optimization #4: Rehashing (dynamic resizing) [M => 2 * M]
        7. Optimization #5: Change collision handling strategy
            I. Linked List -> tree
            II. Open addressing -> Linear Probabing, Quadratic Probabing, Double hashing
    '''

    def __init__(self):
        self.buckets = 100
        self.hashSet = [[] for i in range(self.buckets)]
    
    def getHashKey(self,key: int):
        return key % self.buckets

    def add(self, key: int) -> None:
        index = self.getHashKey(key)
        if key in self.hashSet[index]:
            return False
        else:
            self.hashSet[index].append(key)
            return True

    def remove(self, key: int) -> None:
        index = self.getHashKey(key)
        if key in self.hashSet[index]:
            self.hashSet[index].remove(key)
            return True
        else:
            return False
        

    def contains(self, key: int) -> bool:
        index = self.getHashKey(key)
        if key in self.hashSet[index]:
            return True
        else:
            return False
    
    
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)