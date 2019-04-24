class Solution(object):
    def smallestRangeI(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        min_val = min(A)
        max_val = max(A)
        res = (max_val-K) - (min_val+K)
        return res if res > 0 else 0