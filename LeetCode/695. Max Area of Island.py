class Solution:
    max_num = 0

    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        def bfs(y, x):

            queue = [[y, x]]
            count = 0

            while queue:
                node = queue.pop(0)
                grid[node[0]][node[1]] = 0
                count += 1
                for i, j in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                    if 0 <= node[0] + i < len(grid) and 0 <= node[1] + j < len(grid[0]) and grid[node[0] + i][
                                node[1] + j]:
                        queue.append([node[0] + i, node[1] + j])
                        grid[node[0] + i][node[1] + j] = 0

            self.max_num = max(count, self.max_num)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    bfs(i, j)
        return self.max_num