# DFS
# class Solution(object):
#     minimumSum = float('inf')
#
#     def minimumTotal(self, triangle):
#         """
#         :type triangle: List[List[int]]
#         :rtype: int
#         """
#         if not triangle:
#             return 0
#         root = triangle[0][0]
#         stack = [[0, root, 1]]
#         while stack:
#             n, pathSum, d = stack.pop()
#             if d == len(triangle):
#                 self.minimumSum = min(self.minimumSum, pathSum)
#             else:
#                 stack.append([n, pathSum + triangle[d][n], d + 1])
#                 stack.append([n + 1, pathSum + triangle[d][n + 1], d + 1])
#         return self.minimumSum

#DP Solution
class Solution(object):
    def minimumTotal(self, triangle):
        if not triangle:
            return
        for i in range(len(triangle)-1, -1, -1):
            for j in range(len(triangle[i])):
                triangle[i][j] += min(triangle[i+1][j], triangle[i+1][j+1])
        return triangle[0][0]

