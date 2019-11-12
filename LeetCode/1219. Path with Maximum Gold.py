class Solution(object):
    def getMaximumGold(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        self.max_gold = float('-inf')

        def helper(grid, i, j, visited, path):
            self.max_gold = max(self.max_gold, sum(path))
            if len(path) == 25:
                return
            for y, x in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                if 0 <= i + y < len(grid) and 0 <= j + x < len(grid[0]):
                    if (i + y, j + x) not in visited and grid[i + y][j + x]:
                        visited.add((i + y, j + x))
                        helper(grid, i + y, j + x, visited, path + [grid[i + y][j + x]])
                        visited.remove((i + y, j + x))

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    v = set()
                    v.add((i, j))
                    helper(grid, i, j, v, [grid[i][j]])
        return self.max_gold