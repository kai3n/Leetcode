class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        g = {}
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i == 0 or j == 0:
                    g[j-i] = matrix[i][j]
                else:
                    if matrix[i][j] != g.get(j-i, None):
                        return False
        return True