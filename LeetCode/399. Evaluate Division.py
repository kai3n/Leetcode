class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """

        from collections import defaultdict
        d = defaultdict(lambda: defaultdict(float))
        visited_d = defaultdict()
        res = []

        for i, equation in enumerate(equations):
            visited_d[equation[0]] = 0
            visited_d[equation[1]] = 0
            d[equation[0]][equation[1]] = values[i]
            d[equation[1]][equation[0]] = 1 / values[i]

        for query in queries:
            if not d.get(query[0]) or not d.get(query[1]):
                res.append(-1.0)
                continue
            vd = {i:visited_d[i] for i in visited_d}

            stack = [[query[0], [query[0]]]]
            vd[query[0]] = 1
            isFound = False
            while stack:
                node, path = stack.pop()
                if path[0] == query[0] and path[-1] == query[1]:
                    mul = 1
                    for i in range(len(path)-1):
                        mul *= d[path[i]][path[i+1]]
                    res.append(mul)
                    isFound = True
                    break
                for child in d[node]:
                    if vd[child] == 0:
                        stack.append([child, path+[child]])
                        vd[child] = 1
            if not isFound:
                res.append(-1.0)
        return res


equations = [ ["a", "b"], ["b", "c"] ]
values = [2.0, 3.0]
queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ]

equations = [["a","b"],["c","d"]]
values = [1.0,1.0]
queries = [["a","c"],["b","d"],["b","a"],["d","c"]]

test = Solution()
print(test.calcEquation(equations, values, queries))




