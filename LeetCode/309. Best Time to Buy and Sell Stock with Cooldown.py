class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy = [float('-inf')] * (len(prices)+1)
        sell = [0] * (len(prices)+1)
        rest = [0] * (len(prices)+1)
        for i in range(1, len(prices)+1):
            buy[i] = max(rest[i-1]-prices[i-1], buy[i-1])
            sell[i] = max(buy[i-1]+prices[i-1], sell[i-1])
            rest[i] = max(sell[i-1], buy[i-1], rest[i-1])
        print(buy)
        print(sell)
        print(rest)
        return sell[-1]



prices = [1, 2, 3, 0, 2]
test = Solution()
print(test.maxProfit(prices))