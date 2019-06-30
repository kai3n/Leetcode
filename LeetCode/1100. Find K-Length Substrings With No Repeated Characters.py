class Solution(object):
    def numKLenSubstrNoRepeats(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: int
        """
        if len(S) < K:
            return 0
        c = 0
        d = collections.Counter(S[:K])
        if len(d) == K:
            c += 1
        for i in range(K, len(S)):
            d[S[i-K]] -= 1
            if d[S[i-K]] == 0:
                d.pop(S[i-K])
            d[S[i]] += 1
            if len(d) == K:
                c += 1
        return c