class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        buy = [float('-inf')] * (len(prices)+1)
        sell = [0] * (len(prices)+1)
        for i in range(1, len(prices)+1):
            buy[i] = max(sell[i-1]-prices[i-1], buy[i-1])
            sell[i] = max(buy[i-1]+prices[i-1]-fee, sell[i-1])
        return sell[-1]