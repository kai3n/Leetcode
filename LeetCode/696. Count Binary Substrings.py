class Solution:
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        prevRunLength = 0
        curRunLength = 1
        res = 0

        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                curRunLength += 1
            else:
                prevRunLength = curRunLength
                curRunLength = 1
            if prevRunLength >= curRunLength:
                res += 1
        return res
