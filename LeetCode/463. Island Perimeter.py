class Solution(object):

    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        cnt = 0
        grid2 = [[0 for _ in range(len(grid[0])+2)] for _ in range(len(grid)+2)]
        for i in range(len(grid[0])):
            for j in range(len(grid)):
                grid2[j+1][i+1] = grid[j][i]

        for i in range(len(grid2[0])):
            for j in range(len(grid2)):
                if grid2[j][i] == 1:
                    if grid2[j][i+1] == 0:
                        cnt += 1
                    if grid2[j][i-1] == 0:
                        cnt += 1
                    if grid2[j+1][i] == 0:
                        cnt += 1
                    if grid2[j-1][i] == 0:
                        cnt += 1
                else:
                        continue
        return cnt


grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]

test = Solution()
print(test.islandPerimeter(grid))