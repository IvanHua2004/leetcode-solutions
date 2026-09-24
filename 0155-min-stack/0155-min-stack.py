class MinStack:

    def __init__(self):
        self.stack = []
        self.min = None
        self.last = None

    def push(self, value: int) -> None:
        self.stack.append(value)
        if self.min == None:
            self.min = value
        elif value < self.min:
            self.min = value
        
        self.last = value

    def pop(self) -> None:
        self.stack.pop()
        self.min = min(self.stack) if self.stack else None
        
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()