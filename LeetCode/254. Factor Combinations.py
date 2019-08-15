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

