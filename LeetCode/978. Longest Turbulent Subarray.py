class Solution:
    def maxTurbulenceSize(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if not A:
            return 0

        ret = 1
        down, upwards = 1, 1
        for i in range(1, len(A)):
            if A[i] > A[i - 1]:
                upwards = down + 1
                ret = max(ret, upwards)
                down = 1
            elif A[i] < A[i - 1]:
                down = upwards + 1
                ret = max(ret, down)
                upwards = 1
            else:
                down = 1
                upwards = 1

        return ret