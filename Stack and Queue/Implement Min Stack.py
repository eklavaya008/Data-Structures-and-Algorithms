#Solution

class MinStack(object):
    def __init__(self):
        self.stack = []
        

    def push(self, val):
        if len(self.stack) == 0:
            self.stack.append([val,val])
        else:
            mini = min(self.stack[-1][1],val)
            self.stack.append([val,mini])


    def pop(self):
        if not self.stack:
            return -1
        self.stack.pop()
         

    def top(self):
        if not self.stack:
            return -1
        return self.stack[-1][0]
        

    def getMin(self):
        if not self.stack:
            return 0
        return self.stack[-1][1]
    
