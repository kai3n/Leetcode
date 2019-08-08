class Solution(object):
    memo = {}
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        if self.memo.get(n) is not None:
            return self.memo[n]
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 1
        else:
            res = self.tribonacci(n-1) + self.tribonacci(n-2) + self.tribonacci(n-3)
            self.memo[n] = res
            return res
