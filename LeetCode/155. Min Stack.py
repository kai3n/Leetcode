class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.minNum = float('inf')
        self.stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.minNum = min(self.minNum, x)
        self.stack.append(x)

    def pop(self):
        """
        :rtype: void
        """
        t = self.stack.pop()
        self.minNum = min(self.stack) if len(self.stack) > 0 else float('inf')
        return t

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1] if len(self.stack) > 0 else None

    def getMin(self):
        """
        :rtype: int
        """
        return self.minNum



# Your MinStack object will be instantiated and called as such:
x = 1
obj = MinStack()
obj.push(x)
obj.pop()
param_3 = obj.top()
param_4 = obj.getMin()

minStack = MinStack()
print(minStack.push(-1))
print(minStack.top())
print(minStack.getMin())
# minStack.push(0)
# minStack.push(-3)
# print(minStack.getMin())
# minStack.pop()
# print(minStack.top())
# print(minStack.getMin())