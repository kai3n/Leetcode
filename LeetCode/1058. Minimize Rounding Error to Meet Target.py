class Solution(object):
    def minimizeError(self, prices, target):
        """
        :type prices: List[str]
        :type target: int
        :rtype: str
        """
        arr = [int(float(i)) for i in prices]
        extra = sum([i != float(j) for i,j in zip(arr,prices)])
        if not sum(arr) <= target <= sum(arr) + extra:
            return "-1"
        memo = sorted([float(i) - j for i,j in zip(prices, arr)])
        temp = len(arr) - target + sum(arr)
        return '{:.3f}'.format(sum(memo[:temp]) + len(memo[temp:]) - sum(memo[temp:]))