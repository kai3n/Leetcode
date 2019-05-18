class Solution(object):
    def spiralMatrixIII(self, R, C, r0, c0):
        """
        :type R: int
        :type C: int
        :type r0: int
        :type c0: int
        :rtype: List[List[int]]
        """
        res = [[r0, c0]]
        y, x, n, i = 0, 1, 0, 0
        while len(res) < R * C:
            r0, c0, i = r0 + y, c0 + x, i + 1
            if 0 <= r0 < R and 0 <= c0 < C:
                res.append([r0, c0])
            if i == n / 2 + 1:
                y, x, n, i = x, -y, n + 1, 0
        return res