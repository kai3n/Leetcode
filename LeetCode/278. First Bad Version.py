# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        first = 1
        last = n
        while first <= last:
            mid = (first+last) / 2
            if isBadVersion(mid):
                last = mid - 1
            else:
                first = mid + 1
        return first