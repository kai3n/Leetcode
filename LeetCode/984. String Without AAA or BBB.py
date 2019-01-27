class Solution(object):
    def strWithout3a3b(self, A, B):
        """
        :type A: int
        :type B: int
        :rtype: str
        """
        a = A
        b = B
        res = ""
        while a > 0 or b > 0:
            if a > b:
                if a > 0:
                    res += "a"
                    a -= 1
                    if a > 0:
                        res += "a"
                        a -= 1
                if b > 0:
                    res += "b"
                    b -= 1
            elif b > a:
                if b > 0:
                    res += "b"
                    b -= 1
                    if b > 0:
                        res += "b"
                        b -= 1
                if a > 0:
                    res += "a"
                    a -= 1
            else:
                if a > 0:
                    res += "a"
                    a -= 1
                if b > 0:
                    res += "b"
                    b -= 1

        return res
