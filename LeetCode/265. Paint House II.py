class Solution(object):
    def minCostII(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if not costs:
            return 0
        dp = [[0 for _ in range(len(costs[0]))] for _ in range(len(costs))]
        dp[0] = costs[0]
        for i in range(1, len(dp)):
            for j in range(len(dp[0])):
                dp[i][j] = min(costs[i][j] + dp[i-1][k] for k in range(len(dp[0])) if j != k)
        res = float('inf')
        for i in range(len(dp[0])):
            res = min(res, dp[-1][i])
        return res

# Markov Chain
class Solution(object):
    def minCostII(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if not costs: return 0
        n, k = len(costs), len(costs[0])
        for i in xrange(1, n):
            min1 = min(costs[i-1])
            idx = costs[i-1].index(min1)
            min2 = min(costs[i-1][:idx] + costs[i-1][idx+1:])
            for j in xrange(k):
                if j == idx:
                    costs[i][j] += min2
                else:
                    costs[i][j] += min1
        return min(costs[-1])