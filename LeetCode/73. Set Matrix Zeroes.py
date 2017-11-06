class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        row = [False for _ in range(len(matrix))]
        col = [False for _ in range(len(matrix[0]))]

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    row[i] = True
                    col[j] = True

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                matrix[i][j] = matrix[i][j] if not row[i] and not col[j] else 0

