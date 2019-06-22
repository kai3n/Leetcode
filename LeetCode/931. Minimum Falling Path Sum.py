class Solution(object):
    def minFallingPathSum(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        dp = [[A[i][j] for j in range(len(A[0]))] for i in range(len(A))]

        for i in range(1, len(A)):
            for j in range(len(A[0])):
                dp[i][j] = min(dp[i - 1][k] + dp[i][j] for k in range(len(A[0])) if abs(k - j) <= 1)
        return min(dp[-1])

