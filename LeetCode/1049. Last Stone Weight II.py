class Solution:
    def lastStoneWeightII(self, stones):
        s = sum(stones)
        dp = [0] * (s + 1)
        dp[0] = 1
        for i in range(len(stones)):
            for j in range(len(dp) - 1, -1, -1):
                if j - stones[i] < 0:
                    break
                if dp[j - stones[i]]:
                    dp[j] = 1

        res = s + 1
        for psum in range(1, s + 1):
            if dp[psum] and 2 * psum - s >= 0:
                res = min(res, 2 * psum - s)
        return res