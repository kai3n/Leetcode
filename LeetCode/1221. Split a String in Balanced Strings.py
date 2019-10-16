class Solution(object):
    def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        r = 0
        for c in s:
            if c == "R":
                r += 1
            elif c == "L":
                r -= 1
            if r == 0:
                count += 1
        return count