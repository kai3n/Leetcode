class Solution(object):
    def change(self, amount, coins):
        dp = [0] * (amount + 1)
        dp[0] = 1
        for i in coins:
            for j in range(1, amount+1):
                if j >= i:
                    dp[j] += dp[j - i]
        return dp[amount]

test = Solution()
print(test.change(5, [1,2,5]))


