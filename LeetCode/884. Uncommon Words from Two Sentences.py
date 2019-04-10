class Solution(object):
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        res = []
        c = collections.Counter((A + ' ' + B).split())
        for k, v in c.items():
            if v == 1:
                res.append(k)
        return res