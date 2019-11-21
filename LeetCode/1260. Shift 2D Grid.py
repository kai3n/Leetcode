class Solution(object):
    def shiftGrid(self, grid, k):
        n, m = len(grid), len(grid[0])
        k %= n * m
        r, c = k / m, k % m
        new_grid = [[0 for _ in range(m)] for _ in range(n)]

        for i in range(n):
            for j in range(m):
                x, y = j + c, i + r
                if x >= m:
                    y += 1
                new_grid[y % n][x % m] = grid[i][j]
        return new_grid