class Solution:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        d_s = {}
        d_t = {}
        for ss, tt in zip(s, t):
            if d_s.get(ss, None) == None:
                d_s[ss] = tt
            else:
                if d_s[ss] != tt:
                    return False
            if d_t.get(tt, None) == None:
                d_t[tt] = ss
            else:
                if d_t[tt] != ss:
                    return False
        return True