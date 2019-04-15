class Solution(object):
    def longestArithSeqLength(self, A):
        dp = collections.defaultdict(int)
        for i in xrange(len(A)):
            for j in xrange(i + 1, len(A)):
                a, b = A[i], A[j]
                dp[b - a, j] = max(dp[b - a, j], dp[b - a, i] + 1)
        return max(dp.values()) + 1