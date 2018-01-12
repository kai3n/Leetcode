class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        res = ''
        quotient, remainder = divmod(n, 26)
        if not remainder:
            res = 'Z' + res
            quotient -= 1
        else:
            res = chr(ord('A') + remainder - 1) + res

        while quotient != 0:
            n = quotient
            quotient, remainder = divmod(n, 26)
            if not remainder:
                res = 'Z' + res
                quotient -= 1
            else:
                res = chr(ord('A') + remainder - 1) + res
        return res