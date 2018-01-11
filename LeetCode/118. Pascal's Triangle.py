class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        elif numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1], [1, 1]]

        res = [[1], [1, 1]]
        print(res)
        for i in range(2, numRows):
            row = [1]
            for j in range(1, i):
                row.append(res[-1][j - 1] + res[-1][j])
            row.append(1)
            res.append(row)
        return res

