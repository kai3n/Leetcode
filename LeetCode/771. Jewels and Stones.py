class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        from collections import Counter

        c = Counter(J)
        res = 0
        for e in S:
            if e in c:
                res += 1
        return res