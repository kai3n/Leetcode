class Solution:
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if not nums:
            return 0
        from collections import defaultdict

        d = defaultdict(int)
        for i in nums:
            d[i] += i

        l = sorted(list(d.keys()))

        dp = [0] * len(l)
        dp[0] = d[l[0]]
        if len(nums) == 1:
            return dp[0]
        dp[1] = d[l[0]] + d[l[1]] if l[1] - l[0] > 1 else max(d[l[0]], d[l[1]])
        if len(nums) == 2:
            return dp[1]
        else:
            for i in range(2, len(l)):
                dp[i] = dp[i - 1] + d[l[i]] if l[i] - l[i - 1] > 1 else max(dp[i - 2] + d[l[i]], dp[i - 1])
            return dp[-1]


