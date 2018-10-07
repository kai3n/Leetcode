class Solution:
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        if not S:
            return ""

        l = []
        ret = []
        for c in S:
            if c.isalpha():
                l.append(c)
        l.reverse()

        for c in S:
            if c.isalpha():
                ret.append(l.pop(0))
            else:
                ret.append(c)
        return "".join(ret)

