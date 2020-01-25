class Solution(object):
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """
        table = [[0 for _ in range(n+1)] for _ in range(n+1)]
        def dp(t, s, e):
            if s >= e:
                return 0
            if t[s][e] !=0:
                return t[s][e]
            res = float('inf')
            for x in range(s, e+1):
                tmp = x + max(dp(t, s, x-1), dp(t, x+1, e))
                res = min(res, tmp)
            t[s][e] = res
            return res
        return dp(table, 1, n)