class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = [homepage]
        self.cur = len(self.history) - 1

    def visit(self, url: str) -> None:
        self.history = self.history[:self.cur + 1]
        self.history.append(url)
        self.cur = len(self.history) - 1

    def back(self, steps: int) -> str:
        if steps < self.cur:
            self.cur -= steps
            return self.history[self.cur]
        else:
            self.cur = 0
            return self.history[0]
        
    def forward(self, steps: int) -> str:
        if self.cur + steps < len(self.history):
            self.cur += steps
            return self.history[self.cur]
        else:
            self.cur = len(self.history) - 1
            return self.history[-1]
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
