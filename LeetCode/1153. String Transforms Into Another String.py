class Solution(object):
    def canConvert(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: bool
        """
        if str1 == str2:
            return True
        d = {}
        for s1, s2 in zip(str1, str2):
            if d.get(s1) is not None:
                if d[s1] != s2:
                    return False
            d[s1] = s2
        return len(set(str2)) < 26