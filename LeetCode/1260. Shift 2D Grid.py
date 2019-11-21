class Solution(object):
    def shiftGrid(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        k %= len(grid)*len(grid[0])
        r = k / len(grid[0])
        c = k % len(grid[0])
        print(r, c)
        new_grid = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                x = j + c
                y = i + r
                if x >= len(grid[0]):
                    x -= len(grid[0])
                    y += 1
                new_grid[y%len(grid)][x] = grid[i][j]
        return new_grid