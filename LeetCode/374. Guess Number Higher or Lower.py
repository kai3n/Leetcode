# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        first = 1
        last = n
        while first <= last:
            mid = (first + last) / 2
            r = guess(mid)
            if r == 0:
                return mid
            elif r == 1:
                first = mid + 1
            else:
                last = mid - 1