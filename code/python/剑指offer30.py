class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minstack = []

    def push(self, x: int) -> None:
        if not self.stack:
            self.stack.append(x)
            self.minstack.append(0)
        else:
            self.stack.append(x)
            if x<=self.stack[self.minstack[-1]]:
                self.minstack.append(len(self.stack)-1)

    def pop(self) -> None:
        popd = self.stack[-1]
        if popd==self.stack[self.minstack[-1]]:
            self.minstack.pop()
        self.stack.pop()
        return popd

    def top(self) -> int:
        return self.stack[-1] if self.stack else -1

    def min(self) -> int:
        return self.stack[self.minstack[-1]] if self.minstack else -1


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.min()