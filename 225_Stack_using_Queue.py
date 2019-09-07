class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = []
        

    """
    push 3 -> 2 -> 1  : queue1 : 3 | 2 | 1 
    pop : queue2 : 2 | 1 queue1 : empty
    pop : queue2 : empty queue1 : 1
    """
    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        tempQueue = []
        while len(self.queue) is not 0:
          tempQueue.append(self.queue.pop(0))
        self.queue.append(x)
        while len(tempQueue) is not 0:
          self.queue.append(tempQueue.pop(0))

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.queue.pop(0)

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.queue[0]

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self.queue) is 0
        

# Your MyStack object will be instantiated and called as such:
obj = MyStack()
obj.push(2)
param_2 = obj.pop()
# param_3 = obj.top()
param_4 = obj.empty()

print(param_4)
print(param_2)


