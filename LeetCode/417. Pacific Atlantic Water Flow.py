class Solution(object):

    def __init__(self):
        self.dir = [[0, 1], [0, -1], [1, 0], [-1, 0]]

    def pacificAtlantic(self, matrix):
        res = []
        if matrix == None or len(matrix) == 0 or len(matrix[0]) == 0:
            return res
        n = len(matrix)
        m = len(matrix[0])
        pacific = [[False for _ in range(m)] for _ in range(n)]
        atlantic = [[False for _ in range(m)] for _ in range(n)]

        for i in range(n):
            self.dfs(matrix, pacific, float('-inf'), i, 0)
            self.dfs(matrix, atlantic, float('-inf'), i, m-1)
        for i in range(m):
            self.dfs(matrix, pacific, float('-inf'), 0, i)
            self.dfs(matrix, atlantic, float('-inf'), n-1, i)
        for i in range(n):
            for j in range(m):
                if pacific[i][j] and atlantic[i][j]:
                    res.append([i, j])
        return res

    def dfs(self, matrix, visited, height, x, y):
        n = len(matrix)
        m = len(matrix[0])
        if x < 0 or x >= n or y < 0 or y >= m or visited[x][y] or matrix[x][y] < height:
            return
        visited[x][y] = True
        for d in self.dir:
            self.dfs(matrix, visited, matrix[x][y], x+d[0], y+d[1])