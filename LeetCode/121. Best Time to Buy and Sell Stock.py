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