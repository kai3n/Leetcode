def maxCoins(iNums):
    nums = [1] + [i for i in iNums if i > 0] + [1]
    n = len(nums)
    dp = [[0]*n for _ in range(n)]

    for k in range(2, n):
        for left in range(0, n - k):
            right = left + k
            for i in range(left + 1, right):
                dp[left][right] = max(dp[left][right],
                       nums[left] * nums[i] * nums[right] + dp[left][i] + dp[i][right])

            for i in range(len(dp)):
                for j in range(len(dp[0])):
                    print(dp[i][j], "  ", end="")
                print()
            print()
    return dp[0][n - 1]

nums = [3, 1, 5, 8]
print(maxCoins(nums))
