class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        s = [str(i) for i in range(1, n+1)]
        ss = "".join(s)
        return int(ss[n-1])

    def findNthDigit(self, n):
        n -= 1
        for digits in range(1, 11):
            first = 10 ** (digits - 1)
            if n < 9 * first * digits:
                return int(str(first + n / digits)[n % digits])
            n -= 9 * first * digits

test = Solution()
print(test.findNthDigit(3))