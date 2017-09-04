# Brute Force Solution
# class NumMatrix(object):
#     def __init__(self, matrix):
#         """
#         :type matrix: List[List[int]]
#         """
#         self.matrix = matrix
#
#     def update(self, row, col, val):
#         """
#         :type row: int
#         :type col: int
#         :type val: int
#         :rtype: void
#         """
#         self.matrix[row][col] = val
#
#     def sumRegion(self, row1, col1, row2, col2):
#         """
#         :type row1: int
#         :type col1: int
#         :type row2: int
#         :type col2: int
#         :rtype: int
#         """
#         sum = 0
#         for y in range(row1, row2+1):
#             for x in range(col1, col2+1):
#                 sum += self.matrix[y][x]
#         return sum
#
#
#
# matrix = [
#   [3, 0, 1, 4, 2],
#   [5, 6, 3, 2, 1],
#   [1, 2, 0, 1, 5],
#   [4, 1, 0, 1, 7],
#   [1, 0, 3, 0, 5]
# ]
#
# obj = NumMatrix(matrix)
# print(obj.sumRegion(2, 1, 4, 3))
# obj.update(3, 2, 2)
# print(obj.sumRegion(2, 1, 4, 3))


class NumMatrix(object):

    def __init__(self, matrix):
        self.d = matrix
        for row in matrix:
            for i in range(1, len(row)):
                row[i] += row[i-1]

    def update(self, row, col, val):
        row = self.d[row]
        orig = row[col] - (row[col-1] if col else 0)
        for i in range(col, len(row)):
            row[i] += val - orig

    def sumRegion(self, row1, col1, row2, col2):
        out = 0
        for i in range(row1, row2+1):
            out += self.d[i][col2] - (self.d[i][col1-1] if col1 else 0)
        return out

matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]

obj = NumMatrix(matrix)
print(obj.sumRegion(2, 1, 4, 3))
obj.update(3, 2, 2)
print(obj.sumRegion(2, 1, 4, 3))