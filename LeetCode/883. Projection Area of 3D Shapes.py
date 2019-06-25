class Solution(object):
    def projectionArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        res = 0
        # xy plane
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    res += 1
        # yz plane
        for i in range(len(grid)):
            res += max(grid[i])

        # xz plane
        for i in range(len(grid[0])):
            res += max(grid[j][i] for j in range(len(grid)))
        return res
