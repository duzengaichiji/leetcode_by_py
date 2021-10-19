class CQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def appendTail(self, value: int) -> None:
        self.stack1.append(value)

    def deleteHead(self) -> int:
        #print(self.stack1,self.stack2)
        if not self.stack1 and not self.stack2:
            return -1
        elif self.stack2:
            return self.stack2.pop()
        elif self.stack1 and not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
            return self.stack2.pop()