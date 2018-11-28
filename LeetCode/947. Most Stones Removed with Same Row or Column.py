class Solution:
    def removeStones(self, stones):
        """
        :type stones: List[List[int]]
        :rtype: int
        """
        from collections import defaultdict

        graph = defaultdict(list)
        for i, x in enumerate(stones):
            for j in range(i):
                y = stones[j]
                if x[0] == y[0] or x[1] == y[1]:
                    graph[i].append(j)
                    graph[j].append(i)

        N = len(stones)
        res = 0

        seen = [False] * N
        for i in range(N):
            if not seen[i]:
                stack = [i]
                seen[i] = True
                while stack:
                    res += 1
                    node = stack.pop()
                    for nei in graph[node]:
                        if not seen[nei]:
                            stack.append(nei)
                            seen[nei] = True
                res -= 1
        return res
