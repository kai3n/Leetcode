class Solution(object):
    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """
        return True

class Solution:
    def stoneGame(self, piles):
        N = len(piles)
        self.hash = {}
        def dp(i, j):
            if (i,j) in self.hash:
                return self.hash[(i,j)]
            # The value of the game [piles[i], piles[i+1], ..., piles[j]].
            if i > j: return 0
            parity = (j - i) % 2
            if parity == 1:  # first player
                val = max(piles[i] + dp(i+1,j), piles[j] + dp(i,j-1))
                self.hash[(i,j)] = val
                return val
            else:
                val = min(-piles[i] + dp(i+1,j), -piles[j] + dp(i,j-1))
                self.hash[(i,j)] = val
                return val

        return dp(0, N - 1) > 0