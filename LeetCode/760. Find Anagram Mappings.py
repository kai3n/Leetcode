class Solution:
    def anagramMappings(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        d = {}
        res = []
        for i, e in enumerate(B):
            d[e] = i

        for e in A:
            res.append(d.get(e, -1))
        return res