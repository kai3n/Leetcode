class Solution(object):
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        res = []
        c = float('inf')
        for i in range(len(S)):
            c += 1
            if S[i] == C:
                res.append(0)
                c = 0
            else:
                res.append(c)
        for i in range(len(S)-1, -1, -1):
            c += 1
            if S[i] == C:
                c = 0
            else:
                res[i] = min(res[i], c)
        return res