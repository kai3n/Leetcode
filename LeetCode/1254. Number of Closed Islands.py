class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        def dfs(grid, x, y):
            if 0 <= x < len(grid[0]) and 0 <= y < len(grid):
                if grid[y][x] == 0:
                    grid[y][x] = -1
                    if not (dfs(grid, x + 1, y) and dfs(grid, x, y + 1) and dfs(grid, x - 1, y) and dfs(grid, x,
                                                                                                        y - 1)):
                        grid[y][x] = -2
                if grid[y][x] == -2:
                    return False
                return True
            return False

        for i in range(len(grid)):
            if grid[i][0] == 0:
                grid[i][0] = -2
            if grid[i][-1] == 0:
                grid[i][-1] = -2
        for j in range(len(grid[0])):
            if grid[0][j] == 0:
                grid[0][j] = -2
            if grid[-1][j] == 0:
                grid[-1][j] = -2

        count = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    count += dfs(grid, j, i)
        return count
