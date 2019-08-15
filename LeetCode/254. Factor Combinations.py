class Solution(object):
    def getFactors(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        self.res = set()

        def is_prime(n):
            for i in range(2, (n // 2) + 1):
                if n % i == 0:
                    return False
            return True

        def helper(n, factors, start):
            if is_prime(n):
                if not start:
                    self.res.add(tuple(sorted(factors + [n])))
                return
            for i in range(2, n // 2 + 1):
                if n % i == 0:
                    self.res.add(tuple(sorted(factors + [i] + [n // i])))
                    helper(n // i, factors + [i], False)

        helper(n, [], True)
        return list(self.res)

# different version
import math


class Solution:

    def getFactorsFrom(self, n, frm):
        res = []
        for i in range(frm, int(math.floor(math.sqrt(n))) + 1):
            if n % i == 0:
                res.append([i, n // i])
                for partial in self.getFactorsFrom(n // i, i):
                    res.append([i] + partial)
        return res

    def getFactors(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        return self.getFactorsFrom(n, 2)