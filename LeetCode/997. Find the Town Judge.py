class Solution(object):
    def findJudge(self, N, trust):
        """
        :type N: int
        :type trust: List[List[int]]
        :rtype: int
        """
        if not trust and N == 1:
            return 1
        from collections import defaultdict
        d = defaultdict(list)
        d2 = defaultdict(list)
        for i in range(len(trust)):
            d[trust[i][1]].append(trust[i][0])
            d2[trust[i][0]].append(trust[i][1])
        for k, v in d.items():
            if len(v) == N - 1:
                if d2.get(k) is not None:
                    return -1
                else:
                    return k
        return -1
