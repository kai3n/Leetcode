class Solution:
    def eventualSafeNodes(self, graph):
        def dfs(graph, i, visited):
            for j in graph[i]:
                if j in visited: return False
                if j in ans: continue
                visited.add(j)
                if not dfs(graph, j, visited): return False
                visited.remove(j)
            ans.add(i)
            return True

        ans = set()
        for i in range(len(graph)):
            visited = set([i])
            dfs(graph, i, visited)
        return sorted(list(ans))

test = Solution()
print(test.eventualSafeNodes([[1,2],[2,3],[5],[0],[5],[],[]]))
print(test.eventualSafeNodes([[1,2,3,4],[1,2],[3,4],[0,4],[]]))
