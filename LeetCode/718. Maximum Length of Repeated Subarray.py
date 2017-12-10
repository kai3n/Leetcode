class Solution:
    def findLength(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        max_len = 0
        dp = [[0 for _ in range(len(A) + 1)] for _ in range(len(B) + 1)]

        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                if B[i - 1] == A[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    max_len = max(dp[i][j], max_len)
        return max_len


