class Solution(object):
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a_n, a_i = a.split("+")
        b_n, b_i = b.split("+")

        n = str(int(a_n)*int(b_n) + -1 * (int(a_i[:-1]) * int(b_i[:-1])))
        i = str(int(a_n)*int(b_i[:-1]) + int(b_n)*int(a_i[:-1]))
        return n + "+" + i + "i"


test = Solution()
print(test.complexNumberMultiply("1+1i", "1+1i"))
print(test.complexNumberMultiply("1+-1i", "1+-1i"))