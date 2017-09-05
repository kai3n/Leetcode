class MovingAverage(object):
    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.i = 0
        self.size = size
        self.arr = [0] * size
        self.c = 0

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        if self.c < self.size:
            self.arr[self.i % self.size] = val
            self.c += 1
            self.i += 1
            return sum(self.arr[:self.c]) / float(self.c)
        else:
            self.arr[self.i % self.size] = val
            self.i += 1
            return sum(self.arr) / float(self.size)




# Your MovingAverage object will be instantiated and called as such:
size = 3
obj = MovingAverage(size)
print(obj.next(1))
print(obj.next(10))
print(obj.next(3))
print(obj.next(5))