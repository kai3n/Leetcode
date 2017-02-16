def change(amount, coins):
    """
    :type amount: int
    :type coins: List[int]
    :rtype: int
    """
    dp = [0] * (amount + 1)
    dp[0] = 1
    for i in coins:
        for j in range(1, amount+1):
            if j >= i:
                dp[j] += dp[j - i]
    return dp[amount]


print(change(5, [1,2,5]))

