class Solution(object):
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        if len(A) < 3:
            return True
        init_monotone = None
        for i in range(1, len(A)):
            if init_monotone is None:
                if A[i] > A[i - 1]:
                    init_monotone = True
                elif A[i] < A[i - 1]:
                    init_monotone = False
            elif init_monotone:
                if A[i] < A[i - 1]:
                    return False
            else:
                if A[i] > A[i - 1]:
                    return False
        return True
