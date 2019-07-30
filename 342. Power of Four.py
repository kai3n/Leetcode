class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 1:
            return True
        elif num == 0:
            return False
        elif num % 4 != 0:
            return False
        else:
            return self.isPowerOfFour(num/4)
