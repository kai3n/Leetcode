#Brute Force solution
# class Solution(object):
#     def findLonelyPixel(self, picture):
#         """
#         :type picture: List[List[str]]
#         :rtype: int
#         """
#         count = 0
#         for i in range(len(picture)):
#             for j in range(len(picture[0])):
#                 if picture[i][j] == 'B':
#                     count += self.checkValidity(picture, i, j)
#         return count
#
#     def checkValidity(self, picture, y, x):
#         for j in range(x-1, -1, -1):
#             if 0 <= j < len(picture[0]):
#                 if picture[y][j] == 'B':
#                     return 0
#         for j in range(x+1, len(picture[0])):
#             if 0 <= j < len(picture[0]):
#                 if picture[y][j] == 'B':
#                     return 0
#         for i in range(y-1, -1, -1):
#             if 0 <= i < len(picture):
#                 if picture[i][x] == 'B':
#                     return 0
#         for i in range(y+1, len(picture)):
#             if 0 <= i < len(picture):
#                 if picture[i][x] == 'B':
#                     return 0
#         return 1

class Solution(object):
    def findLonelyPixel(self, picture):
        """
        :type picture: List[List[str]]
        :rtype: int
        """
        l = []
        bCur = []
        res = 0
        for i in range(len(picture)):
            count = 0
            for j in range(len(picture[0])):
                if picture[i][j] == 'B':
                    bCur = [i,j]
                    count += 1
            if count == 1:
                l.append(bCur)
        for y, x in l:
            count = 0
            for i in range(len(picture)):
                if picture[i][x] == 'B':
                    count += 1
            if count == 1:
               res += 1
        return res




board =  [['W', 'W', 'B'],
          ['W', 'B', 'W'],
          ['B', 'W', 'W']]

test = Solution()
print(test.findLonelyPixel(board))