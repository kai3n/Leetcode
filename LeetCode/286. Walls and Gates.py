# def bfs(rooms, y, x):
#     queue = [[y, x]]
#     while queue:
#         n_y, n_x = queue.pop()
#         for i in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
#             if 0 <= n_y+i[0] < len(rooms) and 0 <= n_x+i[1] < len(rooms[0]):
#                 if rooms[n_y + i[0]][n_x + i[1]] > rooms[n_y][n_x]+1:
#                     rooms[n_y + i[0]][n_x + i[1]] = rooms[n_y][n_x]+1
#                     queue.append([n_y + i[0], n_x + i[1]])


class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """

        queue = []
        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j] == 0:
                    queue.append([i, j])
        while queue:
            n_y, n_x = queue.pop()
            for i in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                if 0 <= n_y + i[0] < len(rooms) and 0 <= n_x + i[1] < len(rooms[0]):
                    if rooms[n_y + i[0]][n_x + i[1]] > rooms[n_y][n_x] + 1:
                        rooms[n_y + i[0]][n_x + i[1]] = rooms[n_y][n_x] + 1
                        queue.append([n_y + i[0], n_x + i[1]])

        return rooms

rooms = [[2147483647,-1,0,2147483647],
         [2147483647,2147483647,2147483647,-1],
         [2147483647,-1,2147483647,-1],
         [0,-1,2147483647,2147483647]]

test = Solution()
a = test.wallsAndGates(rooms)

for i in range(len(a)):
    for j in range(len(a[0])):
        print(a[i][j], ' ', end='')
    print()