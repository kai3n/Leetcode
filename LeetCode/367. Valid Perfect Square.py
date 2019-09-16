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

"""
class Solution(object):
    def isPerfectSquare(self, num):
        left = 0
        right = num
        
        while left <= right:
            mid = left + (right-left)//2
            if  mid ** 2 == num:
                return True
            elif mid ** 2 > num:
                right = mid -1
            else:
                left = mid +1
        return False
"""

