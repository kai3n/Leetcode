class Solution(object):
    def minOperations(self, n):
        """
        :type n: int
        :rtype: int
        """
        nn = n // 2
        if n & 1:
            return (1 + nn)*nn
        else:
            return nn**2
