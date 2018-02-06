class Solution(object):
    def findRedundantConnection(self, edges):
        p = {}  # parents

        def find(x):
            return x if p[x] == x else find(p[x])

        def init(x):
            p.setdefault(x, x)

        for e in edges:
            init(e[0])
            init(e[1])
            x = find(e[0])
            y = find(e[1])
            if x == y:
                return e
            p[y] = x

input = [[1,2], [2,3], [3,4], [1,4], [1,5]]
test = Solution()
print(test.findRedundantConnection(input))