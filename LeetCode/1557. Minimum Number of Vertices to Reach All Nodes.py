class Solution(object):
    def findSmallestSetOfVertices(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        inbounds = {x: 0 for x in range(n)}
        res = []
        for edge in edges:
            inbounds.pop(edge[1], None)
        return list(inbounds)
