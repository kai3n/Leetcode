class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if 0 <= i - 1 < len(grid) and 0 <= j - 1 < len(grid[0]):
                    grid[i][j] = min(grid[i][j] + grid[i - 1][j], grid[i][j] + grid[i][j - 1])
                elif 0 <= i - 1 < len(grid):
                    grid[i][j] += grid[i - 1][j]
                elif 0 <= j - 1 < len(grid[0]):
                    grid[i][j] += grid[i][j - 1]
        return grid[-1][-1]