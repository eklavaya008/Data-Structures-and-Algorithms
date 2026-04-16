#Solution

from collections import deque
class MyStack(object):

    def __init__(self):
        self.queue = deque()

    def push(self, x):
        self.queue.append(x)
        for _ in range(len(self.queue)-1):
            self.queue.append(self.queue.popleft())


    def pop(self):
        if not self.queue:
            return "empty stack"
        return self.queue.popleft()
        

    def top(self):
        if not self.queue:
            return "empty stack"
        return self.queue[0]
        

    def empty(self):
        return len(self.queue) == 0
