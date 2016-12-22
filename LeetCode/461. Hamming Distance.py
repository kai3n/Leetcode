class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        cnt = 0
        for _ in range(32):
            if x % 2 != y % 2:
                cnt += 1
            x >>= 1
            y >>= 1
        return cnt
test = Solution()
print(test.hammingDistance(14,16))