class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if not s and not p:
            return True
        elif not s and p:
            if p[0] == "*":
                return self.isMatch(s, p[1:])
            else:
                return False
        elif s and not p:
            return False
        elif s and p:
            if s[0] == p[0] or p[0] == "?":
                return self.isMatch(s[1:], p[1:])
            elif p[0] == "*":
                return self.isMatch(s[1:], p) or self.isMatch(s, p[1:])
            else:
                return False
