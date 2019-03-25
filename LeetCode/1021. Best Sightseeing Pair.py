class Solution(object):
    def maxScoreSightseeingPair(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        res = cur = 0
        for i in range(len(A)):
            res = max(res, cur+A[i])
            cur = max(cur, A[i]) - 1
        return res