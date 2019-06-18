class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if grid[0][0]:
            return -1
        queue = [[(0, 0), 1]]
        grid[0][0] = 1
        while queue:
            node, count = queue.pop(0)
            if node == (len(grid) - 1, len(grid[0]) - 1):
                return count
            for i in [-1, 0, 1]:
                for j in [-1, 0, 1]:
                    if 0 <= node[0] + i < len(grid) and 0 <= node[1] + j < len(grid[0]):
                        if not grid[node[0] + i][node[1] + j]:
                            grid[node[0] + i][node[1] + j] = 1
                            queue.append([(node[0] + i, node[1] + j), count + 1])
        return -1
