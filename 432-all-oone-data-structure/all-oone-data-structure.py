class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
        self.prev = None
        self.strs = set()


class AllOne:

    def __init__(self):
        self.hashMap = {}
        self.head = Node(0)
        self.tail = Node(0)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    # Insert After a node
    def insertNode(self, prev_node, new_node):
        new_node.next = prev_node.next
        new_node.prev = prev_node
        prev_node.next.prev = new_node
        prev_node.next = new_node
    
    # Delete a node
    def deleteNode(self,curr_node):
        curr_node.prev.next = curr_node.next
        curr_node.next.prev = curr_node.prev

    def inc(self, key: str) -> None:
        if key not in self.hashMap:
            if self.head.next.val == 1:
                new_node = self.head.next
            else:
                new_node = Node(1)
                self.insertNode(self.head,new_node)
            self.hashMap[key] = new_node
            new_node.strs.add(key)
        else:
            curr_node = self.hashMap[key]
            if curr_node.next != self.tail and curr_node.next.val == curr_node.val + 1:
                new_node = curr_node.next
            else: 
                new_node = Node(curr_node.val + 1)
                self.insertNode(curr_node,new_node)

            curr_node.strs.remove(key)

            if len(curr_node.strs) == 0:
                self.deleteNode(curr_node)

            self.hashMap[key] = new_node
            new_node.strs.add(key)

    def dec(self, key: str) -> None:
        curr_node = self.hashMap[key]
        curr_node.strs.remove(key)

        if curr_node.val == 1:
            del self.hashMap[key]
            if len(curr_node.strs) == 0:
                self.deleteNode(curr_node)
            return

        if curr_node.prev != self.head and curr_node.prev.val == curr_node.val - 1:
            new_node = curr_node.prev
        else:
            new_node = Node(curr_node.val - 1)
            self.insertNode(curr_node.prev, new_node)
        
        self.hashMap[key] = new_node
        new_node.strs.add(key)
        
        if len(curr_node.strs) == 0:
            self.deleteNode(curr_node)
        

    def getMaxKey(self) -> str:
        if self.tail.prev != self.head:
            curr_node = self.tail.prev
            return next(iter(curr_node.strs))
        else:
            return ""       
        
    def getMinKey(self) -> str:
        if self.head.next != self.tail:
            curr_node = self.head.next
            return next(iter(curr_node.strs))
        else:
            return ""
        


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()