class Solution(object):
    def bitwiseComplement(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N == 0:
            return 1
        if N == 1:
            return 0
        x = 1
        while x < N:
            x *= 2
        return x - N - 1 if x != N else x-1