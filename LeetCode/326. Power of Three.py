class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 1:
            return True

        while n > 3.0:
            n /= 3.0

        if n == 3.0:
            return True
        else:
            return False