class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n == 0:
            return [0]
        elif n == 1:
            return [0,1]
        else:
            res = self.grayCode(n-1)
            x = 2**(n-1)
            for i in range(x-1, -1, -1):
                res.append(res[i]+x)
            return res

test = Solution()
print(test.grayCode(3))

