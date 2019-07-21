class Solution(object):
    def numEquivDominoPairs(self, dominoes):
        """
        :type dominoes: List[List[int]]
        :rtype: int
        """
        d = collections.defaultdict(int)
        res = 0
        for domino in dominoes:
            domino = tuple(domino)
            if d.get(domino) is None:
                if d.get(domino[::-1]) is None:
                    d[domino] += 1
                else:
                    d[domino[::-1]] += 1
            else:
                d[domino] += 1
        for k, v in d.items():
            if v > 1:
                res += v*(v-1)/2
        return res
