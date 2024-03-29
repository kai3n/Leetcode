class Solution(object):
    def leadsToDestination(self, n, edges, source, destination):
        def dfs(i):
            seen.add(i)
            for j in graph[i]:
                if j == i or j in seen or not dfs(j):
                    return False
            seen.discard(i)
            return len(graph[i]) != 0 or i == destination
        graph, seen = collections.defaultdict(set), set()
        for a, b in edges:
            graph[a].add(b)
        return dfs(source)