class Solution(object):
    def maxKilledEnemies(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if len(grid) == 0:
            return 0
        if len(grid[0]) == 0:
            return 0
        UP, LEFT, BOTTOM, RIGHT = [0, 1, 2, 3]
        spots = [[[0, 0, 0, 0] for _ in range(len(grid[0]))] for _ in range(len(grid))]
        y = len(grid)
        x = len(grid[0])

        for i in range(y):
            for j in range(x):
                if grid[i][j] == 'W':
                    continue
                spots[i][j][UP] = (0 if i == 0 else spots[i-1][j][UP]) + (1 if grid[i][j] == 'E' else 0)
                spots[i][j][LEFT] = (0 if j == 0 else spots[i][j-1][LEFT]) + (1 if grid[i][j] == 'E' else 0)

        maxKill = 0
        for i in range(y-1, -1, -1):
            for j in range(x-1, -1, -1):
                if grid[i][j] == 'W':
                    continue
                spots[i][j][BOTTOM] = (0 if i == y-1 else spots[i+1][j][BOTTOM]) + (1 if grid[i][j] == 'E' else 0)
                spots[i][j][RIGHT] = (0 if j == x-1 else spots[i][j+1][RIGHT]) + (1 if grid[i][j] == 'E' else 0)

                if grid[i][j] == '0':
                    maxKill = max(maxKill, spots[i][j][UP] + spots[i][j][LEFT] + spots[i][j][BOTTOM] + spots[i][j][RIGHT])

        return maxKill

test = Solution()
print(test.maxKilledEnemies([['0', 'E', '0', '0'],
                             ['E', '0', 'W', 'E'],
                             ['0', 'E', '0', '0']]))