class Solution(object):
    def canConstruct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: bool
        """
        c = Counter(s)
        pair_count = 0
        unpair_count = 0
        for v in c.values():
            pair_count += v / 2
            unpair_count += v % 2
        if unpair_count <= k <= unpair_count + pair_count:
            return True
        if pair_count + unpair_count <= k <= pair_count*2 + unpair_count:
            return True
        return False
