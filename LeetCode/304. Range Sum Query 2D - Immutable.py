class NumMatrix(object):
    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self.matrix = matrix
        self.colSum = [[matrix[i][j] for j in range(len(matrix[0]))] for i in range(len(matrix))]

        if len(self.matrix) == 0 or len(self.matrix[0]) == 0:
            return None
        for j in range(len(matrix[0])):
            for i in range(1, len(matrix)):
                self.colSum[i][j] += self.colSum[i - 1][j]

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """

        if len(self.matrix) == 0 or len(self.matrix[0]) == 0:
            return None
        res = 0
        for j in range(col1, col2 + 1):
            if row1 - 1 >= 0:
                res += self.colSum[row2][j] - self.colSum[row1 - 1][j]
            else:
                res += self.colSum[row2][j]

        return res

matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]

matrix = [[-1]]
matrix = [[]]
test = NumMatrix(matrix)
print(test.sumRegion(0,0,0,0))