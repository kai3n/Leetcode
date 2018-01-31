class Solution:
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        if c < 0:
            return False

        import math
        left = 0
        right = int(math.sqrt(c))
        while left <= right:
            cur = left ** 2 + right ** 2
            if cur == c:
                return True
            elif cur > c:
                right -= 1
            else:
                left += 1
        return False