class Solution(object):
    def luckyNumbers(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        lucky_rows = [0] * len(matrix)
        lucky_cols = [0] * len(matrix[0])

        for i, row in enumerate(matrix):
            lucky_rows[i] = min(row)
        for j, col in enumerate(zip(*matrix)):
            lucky_cols[j] = max(col)

        return set(lucky_rows) & set(lucky_cols)