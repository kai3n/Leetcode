class Solution:
    def __init__(self):
        self.cache = {}

    def knightProbability(self, N, K, r, c):
        """
        :type N: int
        :type K: int
        :type r: int
        :type c: int
        :rtype: float
        """
        """
        p_K = p_K_still_in*mean(p_K-1)
        e.g. 1/4*1/4 = 2/8 * (2/8 + 2/8)/2 
        """
        if K == 0:
            return 1
        dirs = [(1, 2), (2, 1), (-1, 2), (2, -1), (1, -2), (-2, 1), (-1, -2), (-2, -1)]
        next_rc = [(r + x, c + y) for x, y in dirs if r + x >= 0 and r + x < N and c + y >= 0 and c + y < N]
        p_K_stillIn = len(next_rc) / 8.0
        s = 0
        for rr, cc in next_rc:
            if (K - 1, rr, cc) not in self.cache:
                self.cache[(K - 1, rr, cc)] = self.knightProbability(N, K - 1, rr, cc)
            s += self.cache[(K - 1, rr, cc)]

        return p_K_stillIn * s / (len(next_rc) + 1e-15)