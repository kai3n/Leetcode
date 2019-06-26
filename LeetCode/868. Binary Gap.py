class Solution(object):
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N == 1:
            return 0
        b = bin(N)[2:]
        beg = 0
        end = 1
        diff = 0
        while end < len(b):
            while end < len(b) and b[end] == '0':
                end += 1
            if end < len(b):
                diff = max(diff, end-beg)
                beg = end
                end = beg + 1
        return diff