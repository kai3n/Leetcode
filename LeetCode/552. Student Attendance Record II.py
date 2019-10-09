class Solution(object):
    def checkRecord(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        if n == 1:
            return 3

        mod = 1000000007
        dp = [0 for i in range(n + 1)]
        dp[0], dp[1], dp[2] = 1, 2, 4
        for i in range(3, n + 1):
            dp[i] = (dp[i - 1] + dp[i - 2] + dp[i - 3]) % mod
        res = dp[n]
        for i in xrange(1, n + 1):
            res += dp[i - 1] * dp[n - i] % mod
        res = res % mod
        return res