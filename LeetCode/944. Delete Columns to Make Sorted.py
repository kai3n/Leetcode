class Solution(object):
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        l = 0
        for j in range(len(A[0])):
            f = False
            for i in range(1, len(A)):
                if A[i - 1][j] > A[i][j]:
                    l += 1
                    break
        return l
