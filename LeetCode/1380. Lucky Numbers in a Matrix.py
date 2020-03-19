class Solution(object):
    def luckyNumbers(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        lucky_rows = [0] * len(matrix)
        lucky_cols = [0] * len(matrix[0])
        res = []

        for i, row in enumerate(matrix):
            lucky_rows[i] = min(row)
        for j in range(len(matrix[0])):
            lucky_cols[j] = max(matrix[x][j] for x in range(len(matrix)))

        for y in lucky_rows:
            for x in lucky_cols:
                if y == x:
                    res.append(x)
        return res