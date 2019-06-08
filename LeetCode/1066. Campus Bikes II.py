class Solution(object):
    def assignBikes(self, workers, bikes):
        dic = {}

        def helper(a, b):
            return abs(a[0] - b[0]) + abs(a[1] - b[1])

        def dfs(p, visited):
            if p == len(workers):
                return 0
            if (p, tuple(visited)) in dic:
                return dic[(p, tuple(visited))]
            temp = float('inf')
            for i in range(len(visited)):
                if visited[i] == 0:
                    visited[i] = 1
                    temp = min(temp, helper(bikes[i], workers[p]) + dfs(p + 1, visited))
                    visited[i] = 0
            dic[(p, tuple(visited))] = temp
            return temp

        visited = [0 for _ in range(len(bikes))]
        ans = dfs(0, visited)
        return ans