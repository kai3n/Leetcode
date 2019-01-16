class Solution:
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        di = {}
        i = 1
        while i < len(A):
            for j in range(len(A[0])):
                if di.get(j) == 1 or A[i-1][j] == A[i][j]:
                    continue
                if A[i-1][j] > A[i][j]:
                    di[j] = 1
                    i = 0
                break
            i += 1
        return len(di)
