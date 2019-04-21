class Solution(object):
    def maxSumTwoNoOverlap(self, A, L, M):
        """
        :type A: List[int]
        :type L: int
        :type M: int
        :rtype: int
        """
        acc_list = [0] * len(A)
        acc_list[0] = A[0]
        for i in range(1, len(A)):
            acc_list[i] = acc_list[i - 1] + A[i]
        res = 0
        for i in range(len(A)):
            for j in range(i + L, len(A)):
                if j + M - 1 < len(A):
                    if i == 0:
                        res = max(res, acc_list[i + L - 1] + acc_list[j + M - 1] - acc_list[j - 1])
                    else:
                        res = max(res, acc_list[i + L - 1] - acc_list[i - 1] + acc_list[j + M - 1] - acc_list[j - 1])
        for i in range(len(A)):
            for j in range(i + M, len(A)):
                if j + L - 1 < len(A):
                    if i == 0:
                        res = max(res, acc_list[i + M - 1] + acc_list[j + L - 1] - acc_list[j - 1])
                    else:
                        res = max(res, acc_list[i + M - 1] - acc_list[i - 1] + acc_list[j + L - 1] - acc_list[j - 1])
        return res
