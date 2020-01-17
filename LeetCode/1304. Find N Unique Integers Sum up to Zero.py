class Solution(object):
    def sumZero(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        total = 0
        res = []
        for i in range(n-1):
            res.append(i)
            total += i
        res.append(-total)
        return res