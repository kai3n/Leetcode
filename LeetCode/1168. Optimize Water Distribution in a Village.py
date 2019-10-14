class Solution(object):
    def minCostToSupplyWater(self, n, wells, pipes):
        uf = {i: i for i in xrange(n + 1)}

        def find(x):
            if x != uf[x]:
                uf[x] = find(uf[x])
            return uf[x]

        w = [[c, 0, i] for i, c in enumerate(wells, 1)]
        p = [[c, i, j] for i, j, c in pipes]
        res = 0
        for c, x, y in sorted(w + p):
            x, y = find(x), find(y)
            if x != y:
                uf[find(x)] = find(y)
                res += c
                n -= 1
            if n == 0:
                return res


import collections
import heapq
# Minimum Spanning Tree

# Prim
class Solution:
    def minCostToSupplyWater(self, n, wells, pipes):
        # build graph
        graph = collections.defaultdict(list)
        for u, v, w in pipes:
            graph[u].append([w, v])
            graph[v].append([w, u])
        for i in range(n):
            # No need to point back to 0
            graph[0].append([wells[i], i+1])
            # graph[i+1].append([wells[i], i+1, 0])
        visited = {0}
        edges = graph[0]
        heapq.heapify(edges)
        res = 0
        while len(visited) < n+1 and edges:
            w, v = heapq.heappop(edges)
            if v not in visited:
                res += w
                visited.add(v)
                for edge in graph[v]:
                    if edge[1] not in visited:
                        heapq.heappush(edges, edge)
        return res