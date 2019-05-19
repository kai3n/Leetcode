class Solution(object):
    def longestStrChain(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        d = collections.defaultdict(list)
        res = 1
        for word in words:
            d[len(word)].append([word,1])
        for i in range(2, 16 + 1):
            if d.get(i) is not None and d.get(i-1) is not None:
                for d1, w1 in enumerate(d.get(i)):
                    for d2, w2 in enumerate(d.get(i-1)):
                        if set(map(str, w2[0])).issubset(set(map(str, w1[0]))):
                            d[i][d1][1] = d[i-1][d2][1] + 1
                            res = max(res, d[i][d1][1])
        return res