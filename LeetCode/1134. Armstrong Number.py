class Solution(object):
    def isArmstrong(self, N):
        """
        :type N: int
        :rtype: bool
        """
        l = len(str(N))
        s = 0
        for n in str(N):
            s += int(n) ** l
        return s == N
