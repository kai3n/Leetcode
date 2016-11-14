class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        sLen = len(s)
        sum = 0
        for i, letter in enumerate(s):
            sum += (ord(letter)-64) * (26**(sLen-i-1))
        return sum

test = Solution()
print(test.titleToNumber('AB'))
