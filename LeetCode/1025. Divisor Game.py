class Solution(object):
    def divisorGame(self, N):
        """
        :type N: int
        :rtype: bool
        """
        winner = False
        while N != 1:
            x = 1
            for i in range(1, N-1):
                if N % i == 0:
                    x = i
                    break
            N -= x
            winner ^= True
        return winner