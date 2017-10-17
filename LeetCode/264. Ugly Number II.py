class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return
        if n == 1:
            return 1
        ugly = [1] * n
        i2 = i3 = i5 = 0

        for i in range(1, n):
            x = min(ugly[i2]*2, ugly[i3]*3, ugly[i5]*5)
            ugly[i] = x
            if x == ugly[i2]*2:
                i2 += 1
            if x == ugly[i3]*3:
                i3 += 1
            if x == ugly[i5]*5:
                i5 += 1
        return x
test = Solution()
print(test.nthUglyNumber(2))