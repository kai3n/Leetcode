class Solution(object):
    def baseNeg2(self, x):
        res = []
        while x:
            res.append(x & 1)
            x = -(x >> 1)
        return "".join(map(str, res[::-1] or [0]))
    def base2(self, x):
        res = []
        while x:
            res.append(x & 1)
            x = x >> 1
        return "".join(map(str, res[::-1] or [0]))