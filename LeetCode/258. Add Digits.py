class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        numSum = num % 10

        while num != 0:
            num //= 10
            numSum += num % 10

        return numSum if numSum < 10 else self.addDigits(numSum)

test = Solution()
print(test.addDigits(0))
print(test.addDigits(10))
print(test.addDigits(11))
print(test.addDigits(38))
print(test.addDigits(45))
print(test.addDigits(145615))


