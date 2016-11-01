class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 1:
            return True

        while n > 2.0:
            n /= 2.0

        if n == 2.0:
            return True
        else:
            return False


test = Solution()
print(test.isPowerOfTwo(2))
print(test.isPowerOfTwo(4))
print(test.isPowerOfTwo(8))
print(test.isPowerOfTwo(16))
print(test.isPowerOfTwo(32))
print(test.isPowerOfTwo(1024))
print(test.isPowerOfTwo(3))
print(test.isPowerOfTwo(7))
print(test.isPowerOfTwo(9))
print(test.isPowerOfTwo(10))
print(test.isPowerOfTwo(20))
print(test.isPowerOfTwo(66))


# suggested answer
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n&-n == n and n != 0