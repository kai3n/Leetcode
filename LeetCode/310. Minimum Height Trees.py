class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        d = collections.defaultdict(set)
        for u, v in edges:
            d[u].add(v)
            d[v].add(u)
        s = set(range(n))
        while len(s) > 2:
            leaves = set(i for i in s if len(d[i]) == 1)
            s -= leaves
            for i in leaves:
                for j in d[i]:
                    d[j].remove(i)
        return list(s)