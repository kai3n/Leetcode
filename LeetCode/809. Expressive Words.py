class Solution(object):
    def expressiveWords(self, S, words):
        return sum(self.check(S, W) for W in words)

    def check(self, S, W):
        i, j, n, m = 0, 0, len(S), len(W)
        for i in range(n):
            if j < m and S[i] == W[j]:
                j += 1
            elif S[i - 1:i + 2] != S[i] * 3 and S[i] * 3 != S[i - 2:i + 1]:
                return False
        return j == m