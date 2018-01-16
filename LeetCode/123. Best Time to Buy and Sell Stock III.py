class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy1 = [float('-inf')] * (len(prices) + 1)
        buy2 = [float('-inf')] * (len(prices) + 1)
        sell1 = [0] * (len(prices) + 1)
        sell2 = [0] * (len(prices) + 1)

        for i in range(1, len(prices) + 1):
            buy1[i] = max(-prices[i - 1], buy1[i - 1])
            sell1[i] = max(buy1[i - 1] + prices[i - 1], sell1[i - 1])
            buy2[i] = max(sell1[i - 1] - prices[i - 1], buy2[i - 1])
            sell2[i] = max(buy2[i - 1] + prices[i - 1], sell2[i - 1])

        return sell2[-1]