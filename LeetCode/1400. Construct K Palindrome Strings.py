class Solution(object):
    def canConstruct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: bool
        """
        if len(s) < k:
            return False    
        c = Counter(s)
        unpair_count = 0
        for v in c.values():
            unpair_count += v % 2
        return True if unpair_count <= k else False
