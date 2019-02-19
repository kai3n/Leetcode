class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        min_m = 0
        queue = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append((i, j, 0))

        while queue:
            n_i, n_j, m = queue.pop(0)
            min_m = m
            for dy, dx in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                if 0 <= n_i + dy < len(grid) and 0 <= n_j + dx < len(grid[0]):
                    if grid[n_i + dy][n_j + dx] == 1:
                        grid[n_i + dy][n_j + dx] = 2
                        queue.append((n_i + dy, n_j + dx, m + 1))

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1
        return min_m