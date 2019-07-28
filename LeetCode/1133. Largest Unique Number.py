class Solution(object):
    def largestUniqueNumber(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        return max([-1] + [k for k, v in collections.Counter(A).items() if v == 1])
