class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if len(matrix) == 0: return 0
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if i == 0:
                    matrix[i][j] = int(matrix[i][j])
                    continue
                if matrix[i][j] == '1':
                    matrix[i][j] = matrix[i - 1][j] + int(matrix[i][j])
                else:
                    matrix[i][j] = 0
        return max([self.maxRectangle(row) for row in matrix])

    def maxRectangle(self, hist):
        stk = []
        maxx = 0
        hist.append(0)
        for i in range(len(hist)):
            while len(stk) > 0 and hist[i] < hist[stk[-1]]:
                s = stk.pop()
                if len(stk) == 0:
                    maxx = max(maxx, i * hist[s])
                else:
                    maxx = max(maxx, (i - stk[-1] - 1) * hist[s])
            stk.append(i)
        return maxx