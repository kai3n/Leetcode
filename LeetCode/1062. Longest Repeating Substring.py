class Solution(object):
    def longestRepeatingSubstring(self, S):
        """
        :type S: str
        :rtype: int
        """
        dp = [[0]*(len(S)+1) for _ in range(len(S)+1)]
        res = 0
        for i in range(1, len(dp)):
            for j in range(i+1, len(dp)):
                if S[i-1] == S[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                    res = max(res, dp[i][j])
        return res