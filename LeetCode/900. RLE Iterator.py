class RLEIterator(object):

    def __init__(self, A):
        """
        :type A: List[int]
        """
        self.A = A

    def next(self, n):
        """
        :type n: int
        :rtype: int
        """
        while n > 0:
            if not self.A:
                return -1
            while self.A and self.A[0] < 1:
                if self.A[0] < 1:
                    self.A = self.A[2:]
            if n > self.A[0]:
                n -= self.A[0]
                self.A = self.A[2:]
            elif n < self.A[0]:
                self.A[0] -= n
                return self.A[1]
            else:
                res = self.A[1]
                self.A = self.A[2:]
                return res
        


# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(A)
# param_1 = obj.next(n)
