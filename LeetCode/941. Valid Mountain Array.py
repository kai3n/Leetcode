class Solution(object):
    def validMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        if len(A) < 3:
            return False

        c = 0
        g = 0
        for i in range(1, len(A)):
            if A[i - 1] == A[i]:
                return False
            if c == 0:
                if A[i - 1] > A[i]:
                    c = 1
                else:
                    g = 1
            elif c == 1:
                if A[i - 1] < A[i]:
                    return False
            else:
                return False
        return True if c and g else False

