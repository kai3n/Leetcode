class Solution(object):
    def minSteps(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        res = 0
        s_count = Counter(s)
        t_count = Counter(t)
        for letter in t_count.keys():
            if s_count[letter] and t_count[letter]:
                res += min(s_count[letter], t_count[letter])
        return len(s) - res
        
