class Solution(object):
    def oddCells(self, n, m, indices):
        """
        :type n: int
        :type m: int
        :type indices: List[List[int]]
        :rtype: int
        """
        arr = [[0 for _ in range(m)] for _ in range(n)]
        for (y, x) in indices:
            for i in range(len(arr)):
                arr[i][x] ^= 1
            for j in range(len(arr[0])):
                arr[y][j] ^= 1
        return sum(val for row in arr for val in row)


class Solution(object):
    def oddCells(self, n, m, indices):
        row, col = [False] * n, [False] * m
        for r, c in indices:
            row[r] ^= True
            col[c] ^= True
        return m * sum(row) + n * sum(col) - 2 * sum(row) * sum(col)