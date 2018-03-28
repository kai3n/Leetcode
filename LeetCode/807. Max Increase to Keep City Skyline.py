class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        import numpy as np
        tmp_grid = np.array(grid)

        total = 0
        top_view = [int(max(tmp_grid[:, i])) for i in range(len(tmp_grid[0]))]
        left_view = [int(max(tmp_grid[i, :])) for i in range(len(tmp_grid))]

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] < min(top_view[j], left_view[i]):
                    total += min(top_view[j], left_view[i]) - grid[i][j]
        return total

