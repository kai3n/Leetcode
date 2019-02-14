class Solution(object):
    res = float('inf')

    def brokenCalc(self, X, Y):
        """
        :type X: int
        :type Y: int
        :rtype: int
        """

        ans = 0
        while Y > X:
            if Y % 2:
                Y += 1
            else:
                Y /= 2
            ans += 1
        return ans + X - Y