class Solution(object):
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        i = 0
        line = 1
        unit = 0
        while i < len(S):
            unit += widths[ord(S[i]) - 97]
            if unit > 100:
                unit = 0
                line += 1
                continue
            i += 1
        return [line, unit]

