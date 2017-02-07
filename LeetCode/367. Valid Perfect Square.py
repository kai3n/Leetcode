class Solution(object):
    def isPerfectSquare(self, x):
        """
        :type num: int
        :rtype: bool
        """
        r = x
        while r * r > x:
            print(r)
            r = (r + x / r) / 2
        return r * r == x

test = Solution()
print(test.isPerfectSquare(256))
#  Babylonian method





