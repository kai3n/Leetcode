class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        from collections import defaultdict
        visited = set()
        graph = defaultdict(list)
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        return not self.hasCycle(graph, -1, 0, visited) and len(visited) == n

    def hasCycle(self, graph, parent, node, visited):
        visited.add(node)
        for v in graph[node]:
            if v != parent:
                if v in visited or self.hasCycle(graph, node, v, visited):
                    return True
        return False

class Solution:
    def validTree(self, n, edges):
        parent = list(range(n))
        def find(x):
            return x if parent[x] == x else find(parent[x])
        for e in edges:
            x, y = map(find, e)
            if x == y:
                return False
            parent[x] = y
        return len(edges) == n - 1