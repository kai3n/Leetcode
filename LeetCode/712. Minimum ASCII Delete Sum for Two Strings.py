class Solution:
    def minimumDeleteSum(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        dp = [[0 for _ in range(len(s1) + 1)] for _ in range(len(s2) + 1)]

        for i in range(1, len(dp)):
            dp[i][0] = dp[i - 1][0] + ord(s2[i - 1])

        for i in range(1, len(dp[0])):
            dp[0][i] = dp[0][i - 1] + ord(s1[i - 1])

        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                if s1[j - 1] == s2[i - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j] + ord(s2[i - 1]), dp[i][j - 1] + ord(s1[j - 1]))

        return dp[-1][-1]

