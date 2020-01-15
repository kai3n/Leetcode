class Solution(object):
    def getNoZeroIntegers(self, n):
        for a in range(n):
            b = n - a
            if '0' not in str(a)+str(b):
                return [a, b]