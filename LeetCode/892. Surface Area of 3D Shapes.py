class Solution(object):
    def surfaceArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        res = len(grid)*len(grid[0])*2
        for i in range(len(grid)):
            res += grid[i][0]
            for j in range(1, len(grid[0])):
                res += abs(grid[i][j]-grid[i][j-1])
            res += grid[i][-1]
        for i in range(len(grid[0])):
            res += grid[0][i]
            for j in range(1, len(grid)):
                res += abs(grid[j][i]-grid[j-1][i])
            res += grid[-1][i]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    res -= 2
        return res