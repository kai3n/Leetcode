class Solution(object):
    def clumsy(self, N):
        if N == 0:
            return 0
        if N == 1:
            return 1
        if N == 2:
            return 2
        if N == 3:
            return 6
        return int(N * (N - 1) / (N - 2) + self.helper(N - 3))

    def helper(self, N):
        if N == 0:
            return 0
        if N == 1:
            return 1
        if N == 2:
            return 1
        if N == 3:
            return 1
        return N - (N - 1) * (N - 2) / (N - 3) + self.helper(N - 4)