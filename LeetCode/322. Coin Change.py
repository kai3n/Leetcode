# class Solution(object):
#     def coinChange(self, coins, amount):
#         """
#         :type coins: List[int]
#         :type amount: int
#         :rtype: int
#         """
#
#         if amount == 0:
#             return 0
#         dp = [[0 for _ in range(amount+1)] for _ in range(len(coins))]
#         coins.sort()
#         for i in range(len(coins)):
#             for j in range(amount+1):
#                 if i == 0 and j-coins[i] >= 0:
#                     dp[i][j] = (dp[i][j-coins[i]] + 1) if dp[i][j-coins[i]] != 0 or j-coins[i] == 0 else 0
#                 elif j-coins[i] >= 0:
#                     if dp[i][j - coins[i]] != 0 or j - coins[i] == 0:
#                         dp[i][j] = min(dp[i-1][j], dp[i][j-coins[i]] + 1)
#                 else:
#                     dp[i][j] = dp[i-1][j]
#         print(dp)
#         return dp[-1][-1] if dp[-1][-1] != 0 else -1

class Solution(object):
    def coinChange(self, coins, amount):
        max = amount + 1
        dp = [max]*(amount + 1)
        dp[0] = 0
        for i in range(1, amount+1):
            for j in range(len(coins)):
                if coins[j] <= i:
                    dp[i] = min(dp[i], dp[i-coins[j]] + 1)
        return dp[amount] if dp[amount] <= amount else -1

"""

dp = [0, 1, 1, m, m, m, m, m, m, m, m, m]

dp = [0, m, 1, m+1]



"""

coins = [1, 2, 5]
amount = 11

coins = [2, 5, 10, 1]
amount = 27

coins = [2]
amount = 3

test = Solution()
print(test.coinChange(coins, amount))
"""
  0 1 2 3 4 5 6 7 8 9 10 11
1 0 1 2 3 4 5 6 7 8 9 10 11
2 0 1 1 2 2 3 3 4 4 5 5  6
5 0 1 1 2 2 1 3 4 4 5 2  3

  0 1 2 3
2 0 0 1 0
"""
