class Solution(object):
    def maxSumAfterPartitioning(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        dp = [0]*(len(A)+1)
        for i in range(len(A)):
            cur_max = 0
            for k in range(K):
                if i-k >= 0:
                    cur_max = max(cur_max, A[i-k])
                    dp[i+1] = max(dp[i+1], dp[i-k] + cur_max*(k+1))
        return dp[-1]