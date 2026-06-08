class SnapshotArray:

    def __init__(self, length: int):
        self.snapDict = defaultdict(list)
        self.snaps = 0
        
    def binary_search(self,arr,snap_id):
        l = 0 
        r = len(arr) - 1
        res = 0
        while l <= r:
            m = (l + r) // 2
            if arr[m][0] <= snap_id:
                res = arr[m][1]
                l = m + 1
            else:
                r = m - 1
        return res

    def set(self, index: int, val: int) -> None:
        self.snapDict[index].append((self.snaps,val))
        

    def snap(self) -> int:
        snapid = self.snaps
        self.snaps += 1

        return snapid

    def get(self, index: int, snap_id: int) -> int:
        arr = self.snapDict[index]
        return self.binary_search(arr,snap_id)
        

    
        


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)