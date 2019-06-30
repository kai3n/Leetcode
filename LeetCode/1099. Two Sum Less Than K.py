class Solution(object):
    def twoSumLessThanK(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        res = -1
        for i in range(len(A)-1):
            for j in range(i+1, len(A)):
                if A[i]+A[j] < K:
                    res = max(res, A[i]+A[j])
        return res