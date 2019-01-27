class Solution(object):
    def mincostTickets(self, days, costs):
        """
        :type days: List[int]
        :type costs: List[int]
        :rtype: int
        """

        def last(idx, period):
            for j in range(i - 1, -1, -1):
                if days[j] + period <= days[idx]:
                    return dp[j]
            return 0

        dp = [0] * len(days)
        for i in range(len(days)):
            dp[i] = min(costs[0] + last(i, 1), costs[1] + last(i, 7), costs[2] + last(i, 30))

        return dp[-1]
