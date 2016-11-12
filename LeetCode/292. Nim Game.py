class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """

        return True if n % 4 != 0 else False

test = Solution()
print(test.canWinNim(0))
print(test.canWinNim(1))
print(test.canWinNim(2))
print(test.canWinNim(4))
print(test.canWinNim(7))
print(test.canWinNim(8))