# time limit
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        if len(prices) >= 2:
            max = 0
            for i in range(len(prices)):
                for j in range(i, len(prices)):
                    if prices[j] - prices[i] > max:
                        max = prices[j] - prices[i]
            return max
        else:
            return 0




testcase = [7, 1, 5, 3, 6, 4]
test = Solution()
print(test.maxProfit(testcase))  # must be 5.