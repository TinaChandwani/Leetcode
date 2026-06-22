class BrowserHistory:

    def __init__(self, homepage: str):
        self.hDict = {0:homepage}
        self.curr = 0
        self.top = 0

    def visit(self, url: str) -> None:
        while self.top > self.curr:
            del self.hDict[self.top]
            self.top -= 1

        self.curr += 1
        self.top = self.curr
        self.hDict[self.curr] = url
        
    def back(self, steps: int) -> str:
        diff = self.curr - steps
        if diff in self.hDict:
            ans = self.hDict[diff]
            self.curr = diff
        else:
            ans = self.hDict[0]
            self.curr = 0 
        
        return ans
        
    def forward(self, steps: int) -> str:
        diff = self.curr + steps
        if diff in self.hDict:
            ans = self.hDict[diff]
            self.curr = diff
        else:
            ans = self.hDict[self.top]
            self.curr = self.top
        
        return ans


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)