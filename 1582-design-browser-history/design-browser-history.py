class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None
    
class BrowserHistory:
    def __init__(self, homepage: str):
        self.head = Node(homepage)
        self.current = self.head 

    def visit(self, url: str) -> None:
        new_node = Node(url)
        self.current.next = new_node
        new_node.prev = self.current
        self.current = new_node

    def back(self, steps: int) -> str:
        for i in range(steps):
            if self.current.prev:
                self.current = self.current.prev
        
        return self.current.val
        

    def forward(self, steps: int) -> str:
        for i in range(steps):
            if self.current.next:
                self.current = self.current.next
        
        return self.current.val
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)