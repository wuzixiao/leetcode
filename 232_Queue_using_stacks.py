class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.inputStack = []
        self.outputStack = []
        
    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.inputStack.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if len(self.outputStack) is not 0:
            return self.outputStack.pop()
        else :
            while len(self.inputStack) is not 0:
                self.outputStack.append(self.inputStack.pop())
            return self.outputStack.pop()
        
    def peek(self) -> int:
        """
        Get the front element.
        """
        if len(self.outputStack) is not 0:
            return self.outputStack[-1]
        else :
            while len(self.inputStack) is not 0:
                self.outputStack.append(self.inputStack.pop())
        
        return self.outputStack[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.inputStack) is 0 and len(self.outputStack) is 0

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()