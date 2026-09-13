class MyQueue:

    def __init__(self):
        self.stack=[]
        self.stack2=[]
        

    def push(self, x: int) -> None:
        self.stack.append(x)
        

    def pop(self) -> int:
        for i in range(len(self.stack)-1):
            self.stack2.append(self.stack.pop())
        res = self.stack.pop()
        while self.stack2:
            self.stack.append(self.stack2.pop())
        return res

        

    def peek(self) -> int:
        return self.stack[0]


    def empty(self) -> bool:
        if len(self.stack)==0 and len(self.stack2)==0 :
            return True
        else:
            return False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()