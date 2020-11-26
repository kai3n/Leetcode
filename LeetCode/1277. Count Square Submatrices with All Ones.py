class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        res = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if 1 <= i < len(matrix) and 1 <= j < len(matrix[0]):
                    if matrix[i][j]:
                        matrix[i][j] += min(matrix[i - 1][j], matrix[i][j - 1], matrix[i - 1][j - 1])
                res += matrix[i][j]
        return res
