# class Solution:
#     def removeStones(self, stones):
#         """
#         :type stones: List[List[int]]
#         :rtype: int
#         """
#         from collections import defaultdict
#
#         graph = defaultdict(list)
#         for i, x in enumerate(stones):
#             for j in range(i):
#                 y = stones[j]
#                 if x[0] == y[0] or x[1] == y[1]:
#                     graph[i].append(j)
#                     graph[j].append(i)
#
#         N = len(stones)
#         res = 0
#
#         seen = [False] * N
#         for i in range(N):
#             if not seen[i]:
#                 stack = [i]
#                 seen[i] = True
#                 while stack:
#                     res += 1
#                     node = stack.pop()
#                     for nei in graph[node]:
#                         if not seen[nei]:
#                             stack.append(nei)
#                             seen[nei] = True
#                 res -= 1
#         return res


class DSU:
    def __init__(self, N):
        self.p = [i for i in range(N)]

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)
        self.p[x_root] = y_root


class Solution:
    def removeStones(self, stones):
        """
        :type stones: List[List[int]]
        :rtype: int
        """

        N = len(stones)
        dsu = DSU(20000)
        for x, y in stones:
            dsu.union(x, y + 10000)

        return N - len({dsu.find(x) for x, y in stones})