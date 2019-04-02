class Solution(object):
    d ={0:0, 1:1}
    def fib(self, n):
        """
        :type N: int
        :rtype: int
        """
        if self.d.get(n) is not None:
            return self.d[n]
        self.d[n] = self.fib(n-1) + self.fib(n-2)
        return self.d[n]