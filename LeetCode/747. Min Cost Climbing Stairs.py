class Solution:
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        if len(cost) == 2:
            return min(cost)
        dp = [0] * (len(cost) + 1)
        dp[0] = cost[0]
        dp[1] = cost[1]
        for i in range(2, len(dp) - 1):
            dp[i] = min(dp[i - 1] + cost[i], dp[i - 2] + cost[i])
        print(dp)
        return min(dp[-2], dp[-3])
