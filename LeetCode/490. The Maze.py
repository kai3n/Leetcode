class Solution(object):
    def hasPath(self, maze, start, destination):
        maze[start[0]][start[1]] = 2
        queue = [start]

        while queue:
            i, j = queue.pop(0)

            if i == destination[0] and j == destination[1]:
                return True

            for x, y in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                row = i + x
                col = j + y
                while 0 <= row < len(maze) and 0 <= col < len(maze[0]) and maze[row][col] != 1:
                    row += x
                    col += y
                row -= x
                col -= y
                if maze[row][col] == 0:
                    maze[i][j] = 2
                    queue.append([row, col])

        return False