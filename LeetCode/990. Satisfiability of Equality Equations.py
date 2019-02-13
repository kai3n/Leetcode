class Solution(object):
    def equationsPossible(self, equations):
        """
        :type equations: List[str]
        :rtype: bool
        """
        from collections import defaultdict

        graph = defaultdict(set)
        not_equal = list()

        def is_equal(a, b, visited):
            if a == b:
                return True
            visited.add(a)
            for adj in graph[a]:
                if adj in visited:
                    continue
                else:
                    if is_equal(adj, b, visited):
                        return True
            return False

        for a, e, _, b in equations:
            if e == '!':
                not_equal.append((a, b))
            else:
                graph[a].add(b)
                graph[b].add(a)
        for a, b in not_equal:
            if is_equal(a, b, set()):
                return False
        return True