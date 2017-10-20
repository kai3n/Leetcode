class Solution(object):
    def shortestDistance(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: int
        """
        dist = [[-1 for _ in range(len(maze[0]))] for _ in range(len(maze))]
        queue = [[start[0], start[1]]]
        dist[start[0]][start[1]] = 0

        while queue:
            n = queue.pop(0)
            left = right = up = down = 0
            while n[1]-left >= 0 and maze[n[0]][n[1]-left] == 0:
                left += 1
            left -= 1
            while n[1]+right < len(maze[0]) and maze[n[0]][n[1]+right] == 0:
                right += 1
            right -= 1
            while n[0]-up >= 0 and maze[n[0]-up][n[1]] == 0:
                up += 1
            up -= 1
            while n[0]+down < len(maze) and maze[n[0]+down][n[1]] == 0:
                down += 1
            down -= 1
            if dist[n[0]][n[1]-left] == -1 or dist[n[0]][n[1]-left] > dist[n[0]][n[1]] + left:
                dist[n[0]][n[1]-left] = dist[n[0]][n[1]] + left
                queue.append([n[0], n[1]-left])
            if dist[n[0]][n[1]+right] == -1 or dist[n[0]][n[1]+right] > dist[n[0]][n[1]] + right:
                dist[n[0]][n[1]+right] = dist[n[0]][n[1]] + right
                queue.append([n[0], n[1] + right])
            if dist[n[0]-up][n[1]] == -1 or dist[n[0]-up][n[1]] > dist[n[0]][n[1]] + up:
                dist[n[0]-up][n[1]] = dist[n[0]][n[1]] + up
                queue.append([n[0]- up, n[1]])
            if dist[n[0]+down][n[1]] == -1 or dist[n[0]+down][n[1]] > dist[n[0]][n[1]] + down:
                dist[n[0]+down][n[1]] = dist[n[0]][n[1]] + down
                queue.append([n[0] + down, n[1]])
        return dist[destination[0]][destination[1]]



maze =[[0,0,1,0,0],
       [0,0,0,0,0],
       [0,0,0,1,0],
       [1,1,0,1,1],
       [0,0,0,0,0]]

start = [0,4]
destination = [4,4]

test = Solution()
print(test.shortestDistance(maze, start, destination))