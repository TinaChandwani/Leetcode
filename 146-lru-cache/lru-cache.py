class Node:
    def __init__(self,key,val):
        self.val = val
        self.key = key
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.head = Node(None,None)
        self.tail = None

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        else:
            node = self.cache[key]
            if node.next:
                node.next.prev = node.prev
            else:
                self.tail = node.prev
            node.prev.next = node.next
            node.prev = self.head
            node.next = self.head.next
            if self.head.next:
                self.head.next.prev = node
            else:
                self.tail = node
            self.head.next = node
            return node.val

        

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            new_node = Node(key,value)
            self.cache[key] = new_node
            new_node.prev = self.head
            if self.head.next is None:
                # We are inserting the first ele
                self.head.next = new_node
                self.tail = self.head.next
            else:
                new_node.next = self.head.next
                self.head.next.prev = new_node
                self.head.next = new_node
            if self.capacity < len(self.cache):
                # Remove the last element in LL and from hashmap
                lru = self.tail
                self.tail = self.tail.prev
                self.tail.next = None
                del self.cache[lru.key]
        else:
            # Update the value of that node and put it in front
            node = self.cache[key]
            node.val = value
            v = self.get(key)





        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)