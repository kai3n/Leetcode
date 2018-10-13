# class Solution(object):
#     def numIslands(self, grid):
#         """
#         :type grid: List[List[str]]
#         :rtype: int
#         """
#         def dfs(grid, y, x):
#             stack = []
#             stack.append([y, x])
#             while stack:
#                 cur_y, cur_x = stack.pop()
#                 for i, j in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
#                     if 0 <= cur_y+i < len(grid) and 0 <= cur_x+j < len(grid[0]) and grid[cur_y+i][cur_x+j] == '1':
#                         grid[cur_y + i][cur_x + j] = '0'
#                         stack.append([cur_y+i, cur_x+j])
#
#         count = 0
#         for y in range(len(grid)):
#             for x in range(len(grid[0])):
#                 if grid[y][x] == '1':
#                     grid[y][x] = '0'
#                     dfs(grid, y, x)
#                     count += 1
#                 else:
#                     continue
#         return count


class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        count = 0

        def helper(grid, y, x):
            if 0 <= y < len(grid) and 0 <= x < len(grid[0]):
                if grid[y][x] == '1':
                    grid[y][x] = '-1'
                    for i, j in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                        helper(grid, y + i, x + j)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    helper(grid, i, j)
                    count += 1
        return count

test = Solution()
print(test.numIslands([['1','1','1','1','0'],
                     ['1','1','0','1','0'],
                     ['1','1','0','0','0'],
                     ['1','1','0','0','0'],
                     ['0','0','0','0','0']]))
print(test.numIslands([['1','1','0','0','0'],
                     ['1','1','0','0','0'],
                     ['1','1','0','0','0'],
                     ['0','0','1','0','0'],
                     ['0','0','0','1','1']]))

