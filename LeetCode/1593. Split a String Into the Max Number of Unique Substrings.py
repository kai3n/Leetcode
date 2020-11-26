class Solution(object):
    def maxUniqueSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        seen = set()
        def helper(s, seen):
            res = 0
            if s:
                for i in range(1, len(s) + 1):
                    candidate = s[:i]
                    if candidate not in seen:
                        seen.add(candidate)
                        res = max(res, 1 + helper(s[i:], seen))
                        seen.remove(candidate)
            return res
        return helper(s, seen)
        
