# Kadane's Algorithm
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        maxCur = 0
        maxSoFar = 0
        for i in range(1, len(prices)):
            maxCur += prices[i] - prices[i - 1]
            maxCur = max(0, maxCur)
            maxSoFar = max(maxCur, maxSoFar)
        return maxSoFar



testcase = [7, 1, 5, 1, 2, 6, 4]
test = Solution()
print(test.maxProfit(testcase))  # must be 5.

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        l  = max_profit = 0
        r = 1
        while r < len(prices):
            if prices[r] - prices[l] > 0:
                max_profit = max(prices[r] - prices[l], max_profit)
                r += 1
            else:
                l = r
                r += 1
        return max_profit
