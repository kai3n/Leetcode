class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 1
        elif n == 1:
            return 10
        else:
            mul = 9
            for i in range(9,9-n+1,-1):
                mul *= i
            return mul + self.countNumbersWithUniqueDigits(n-1)

test = Solution()
print(test.countNumbersWithUniqueDigits(0))
print(test.countNumbersWithUniqueDigits(1))
print(test.countNumbersWithUniqueDigits(2))
print(test.countNumbersWithUniqueDigits(3))
print(test.countNumbersWithUniqueDigits(4))
