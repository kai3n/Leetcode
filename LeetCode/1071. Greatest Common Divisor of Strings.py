class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        min_len = min(len(str1), len(str2))
        largest = ""
        for i in range(1, min_len + 2):
            if str1[:i] == str2[:i]:
                if len(str1) % len(str1[:i]) == 0 and len(str2) % len(str2[:i]) == 0:
                    if (str1[:i]*(len(str1) / len(str1[:i])) == str1) and (str2[:i]*(len(str2) / len(str2[:i])) == str2):
                        largest = str1[:i]
        return largest